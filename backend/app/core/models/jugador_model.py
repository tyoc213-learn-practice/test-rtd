from decimal import Decimal
from typing import List
from pydantic import BaseModel


class JugadorModel(BaseModel):
    nombre: str
    nivel: str
    goles: int
    sueldo: int
    bono: int
    sueldo_completo: int | None
    equipo: str


class NivelModel(BaseModel):
    nivel: str
    goles_minimos: int


class Jugadores(BaseModel):
    jugadores: List[JugadorModel]
    niveles: List[NivelModel] | None

    class Config:
        schema_extra = {
            "example": {
                "niveles": [
                    {"nivel": "A", "goles_minimos": 5},
                    {"nivel": "B", "goles_minimos": 10},
                    {"nivel": "C", "goles_minimos": 15},
                    {"nivel": "Cuauh", "goles_minimos": 20},
                ],
                "jugadores": [
                    {
                        "nombre": "Juan",
                        "nivel": "A",
                        "goles": 6,
                        "sueldo": 50_000,
                        "bono": 15_000,
                        "sueldo_completo": None,
                        "equipo": "rojo",
                    },
                    {
                        "nombre": "Pedro",
                        "nivel": "B",
                        "goles": 9,
                        "sueldo": 60_000,
                        "bono": 20_000,
                        "sueldo_completo": None,
                        "equipo": "rojo",
                    },
                    {
                        "nombre": "Martín",
                        "nivel": "C",
                        "goles": 10,
                        "sueldo": 70_000,
                        "bono": 25_000,
                        "sueldo_completo": None,
                        "equipo": "rojo",
                    },
                    {
                        "nombre": "Luis",
                        "nivel": "Cuauh",
                        "goles": 30,
                        "sueldo": 100_000,
                        "bono": 50_000,
                        "sueldo_completo": None,
                        "equipo": "rojo",
                    },
                    {
                        "nombre": "Carlos",
                        "nivel": "Cuauh",
                        "goles": 6,
                        "sueldo": 100_000,
                        "bono": 15_000,
                        "sueldo_completo": None,
                        "equipo": "azul",
                    },
                    {
                        "nombre": "Peter",
                        "nivel": "C",
                        "goles": 9,
                        "sueldo": 70_000,
                        "bono": 20_000,
                        "sueldo_completo": None,
                        "equipo": "azul",
                    },
                    {
                        "nombre": "Francisco",
                        "nivel": "B",
                        "goles": 10,
                        "sueldo": 60_000,
                        "bono": 25_000,
                        "sueldo_completo": None,
                        "equipo": "azul",
                    },
                    {
                        "nombre": "Jair",
                        "nivel": "A",
                        "goles": 30,
                        "sueldo": 50_000,
                        "bono": 50_000,
                        "sueldo_completo": None,
                        "equipo": "azul",
                    },
                ],
            }
        }


class JugadorSueldoModel(BaseModel):
    nombre: str
    goles_minimos: int
    goles: int
    sueldo: int
    bono: int
    sueldo_completo: float
    equipo: str


class JugadoresConSueldo(BaseModel):
    jugadores: List[JugadorSueldoModel]
