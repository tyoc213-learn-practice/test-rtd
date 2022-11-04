from fastapi.testclient import TestClient
from app.api.fapi import app

client = TestClient(app)


def test_post_sueldo_empty():
    req_args = {
        "jugadores": [],
        "niveles": [{"nivel": "A", "goles_minimos": 5}],
    }
    response = client.post("/api/sueldo/", json=req_args)
    assert response.status_code == 200
    assert {"jugadores": []} == response.json()


def test_post_sueldo_unico():
    req_args = {
        "jugadores": [
            {
                "nombre": "El Rulo",
                "nivel": "B",
                "goles": 9,
                "sueldo": 30000,
                "bono": 15000,
                "sueldo_completo": None,
                "equipo": "rojo",
            },
        ],
        "niveles": [
            {"nivel": "A", "goles_minimos": 5},
            {"nivel": "B", "goles_minimos": 10},
            {"nivel": "C", "goles_minimos": 15},
            {"nivel": "Cuauh", "goles_minimos": 20},
        ],
    }
    response = client.post("/api/sueldo/", json=req_args)
    assert response.status_code == 200
    assert {
        "jugadores": [
            {
                "nombre": "El Rulo",
                "goles_minimos": 10,
                "goles": 9,
                "sueldo": 30000,
                "bono": 15000,
                "sueldo_completo": 43500,
                "equipo": "rojo",
            },
        ]
    } == response.json()


def test_post_json_excel():
    req_args = {
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
    response = client.post("/api/sueldo/", json=req_args)
    assert response.status_code == 200
    assert {
        "jugadores": [
            {
                "nombre": "Juan",
                "goles_minimos": 5,
                "goles": 6,
                "sueldo": 50_000,
                "bono": 15_000,
                "sueldo_completo": round(50_000 + 15_000 * 0.8916746667, 2),
                "equipo": "rojo",
            },
            {
                "nombre": "Pedro",
                "goles_minimos": 10,
                "goles": 9,
                "sueldo": 60_000,
                "bono": 20_000,
                "sueldo_completo": 77833.5,
                "equipo": "rojo",
            },
            {
                "nombre": "Martín",
                "goles_minimos": 15,
                "goles": 10,
                "sueldo": 70_000,
                "bono": 25_000,
                "sueldo_completo": 92291.88,
                "equipo": "rojo",
            },
            {
                "nombre": "Luis",
                "goles_minimos": 20,
                "goles": 30,
                "sueldo": 100_000,
                "bono": 50_000,
                "sueldo_completo": 144583.75,
                "equipo": "rojo",
            },
            {
                "nombre": "Carlos",
                "goles_minimos": 20,
                "goles": 6,
                "sueldo": 100_000,
                "bono": 15_000,
                "sueldo_completo": 110875.0,
                "equipo": "azul",
            },
            {
                "nombre": "Peter",
                "goles_minimos": 15,
                "goles": 9,
                "sueldo": 70_000,
                "bono": 20_000,
                "sueldo_completo": 84500.0,
                "equipo": "azul",
            },
            {
                "nombre": "Francisco",
                "goles_minimos": 10,
                "goles": 10,
                "sueldo": 60_000,
                "bono": 25_000,
                "sueldo_completo": 78125.0,
                "equipo": "azul",
            },
            {
                "nombre": "Jair",
                "goles_minimos": 5,
                "goles": 30,
                "sueldo": 50_000,
                "bono": 50_000,
                "sueldo_completo": 86250.0,
                "equipo": "azul",
            },
        ]
    } == response.json()
