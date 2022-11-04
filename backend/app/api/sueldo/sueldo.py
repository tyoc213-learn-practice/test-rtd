import logging
from fastapi import APIRouter

from app.core.models.jugador_model import Jugadores
from app.core.models.jugador_model import JugadoresConSueldo
from app.core.actions.payment_calculator import PaymentCalculator

router = APIRouter()


@router.get("/")
async def root():
    return {}


@router.post("/", response_model=JugadoresConSueldo)
async def handle_sueldo(data: Jugadores):
    """Procesa la peticion y devuelve el resultado calculando `sueldo_completo` para cada jugador

    Se pude pasar una lista de niveles donde se puede cambiar los valores default o agregar nuevos.

    data: Puede contener la lista de jugadores y la lista de niveles que es opcional"""
    logging.debug(data)
    # niveles default
    d = {"A": 5, "B": 10, "C": 15, "Cuauh": 20}
    if data.niveles is not None and len(data.niveles) > 0:
        d = {d.nivel: d.goles_minimos for d in data.niveles}
    return PaymentCalculator(data, d).do()
