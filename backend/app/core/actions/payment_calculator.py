from dataclasses import dataclass
from functools import reduce
import logging
from typing import List

from app.core.models.jugador_model import JugadorModel
from app.core.models.jugador_model import JugadoresConSueldo
from app.core.models.jugador_model import Jugadores
from app.core.models.jugador_model import JugadorSueldoModel


@dataclass
class PaymentCalculator:
    lista: Jugadores
    equivalencias: dict()
    DEFAULT_MINIMO = 100

    def _reducir_goles(self, d, jugador: JugadorModel):
        """Por equipo acumula en `d` los goles actuales y esperados del `jugador`"""
        logging.debug(f"_reducir_goles({d, jugador})")
        equivalencia = self.equivalencias.get(jugador.nivel, self.DEFAULT_MINIMO)
        ju_ind = jugador.equipo not in d
        pct_individual = round(min(1.0, jugador.goles / equivalencia), 4)
        d[jugador.equipo] = {
            "jugaron": 1 if ju_ind else d[jugador.equipo]["jugaron"] + 1,
            "total_pct": pct_individual
            if ju_ind
            else d[jugador.equipo]["total_pct"] + pct_individual,
        }
        return d

    def _generar_elemento(self, jugador: JugadorModel, equipos):
        """Genera un `JugadorSueldoModel` teniendo los goles acumulados y esperados en los `equipos` del `jugador`"""
        logging.debug(f"_generar_elemento({jugador, equipos})")
        pct_equipo = (
            equipos[jugador.equipo]["total_pct"] / equipos[jugador.equipo]["jugaron"]
        )
        completo = round(jugador.sueldo + pct_equipo * jugador.bono, 2)
        return JugadorSueldoModel(
            nombre=jugador.nombre,
            goles_minimos=self.equivalencias.get(jugador.nivel, self.DEFAULT_MINIMO),
            goles=jugador.goles,
            sueldo=jugador.sueldo,
            bono=jugador.bono,
            sueldo_completo=completo,
            equipo=jugador.equipo,
        )

    def do(self) -> JugadoresConSueldo:
        """Genera por jugador su `sueldo_completo` y `goles_minimos`

        1. Calcular los totales de goles esperados y actuales por equipo con `reduce`.
        2. Con los totales calcular el performance por jugador y generar su elemento.
        """
        equipos = reduce(
            lambda a, b: self._reducir_goles(a, b), self.lista.jugadores, {}
        )
        jugadores = list(
            map(lambda a: self._generar_elemento(a, equipos), self.lista.jugadores)
        )
        return JugadoresConSueldo(jugadores=jugadores)
