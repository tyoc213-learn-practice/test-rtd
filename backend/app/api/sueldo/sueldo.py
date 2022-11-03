from typing import List
from fastapi import APIRouter

from app.core.models.jugador_model import Jugadores
from app.core.models.jugador_model import JugadoresConSUeldo

router = APIRouter()


@router.get("/")
async def root():
    return {}


@router.post("/", response_model=JugadoresConSUeldo)
async def handle_sueldo(data: Jugadores):
    return {"jugadores": []}
