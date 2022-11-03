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

    def _reducir_goles(self, d, jugador: JugadorModel):
        """Por equipo acumula en `d` los goles actuales y esperados del `jugador`"""
        logging.debug(f"_reducir_goles({d, jugador})")
        equivalencia = self.equivalencias[jugador.nivel]
        d[jugador.equipo] = {
            "goles": jugador.goles
            if jugador.equipo not in d
            else d[jugador.equipo]["goles"] + jugador.goles,
            "esperado": equivalencia
            if jugador.equipo not in d
            else d[jugador.equipo]["esperado"] + equivalencia,
        }
        return d

    def _generar_elemento(self, jugador: JugadorModel, equipos):
        """Genera un `JugadorSueldoModel` teniendo los goles acumulados y esperados en los `equipos` del `jugador`"""
        logging.debug(f"_generar_elemento({jugador, equipos})")
        equivalencia = self.equivalencias[jugador.nivel]
        pct_individual = min(1.0, jugador.goles / self.equivalencias[jugador.nivel])
        pct_equipo = min(
            1.0,
            equipos[jugador.equipo]["goles"] / equipos[jugador.equipo]["esperado"],
        )
        completo = jugador.sueldo + (0.5 * (pct_individual + pct_equipo) * jugador.bono)
        return JugadorSueldoModel(
            nombre=jugador.nombre,
            goles_minimos=equivalencia,
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
