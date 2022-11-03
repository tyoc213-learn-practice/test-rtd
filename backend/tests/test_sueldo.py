from fastapi.testclient import TestClient
from app.api.fapi import app

client = TestClient(app)


def test_post_sueldo_empty():
    req_args = {"jugadores": []}
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
        ]
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
