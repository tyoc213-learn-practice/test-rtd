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
    logging.debug(data)
    return PaymentCalculator(data, {"A": 5, "B": 10, "C": 15, "Cuauh": 20}).do()
