from fastapi.testclient import TestClient
from app.api.fapi import app

client = TestClient(app)


def test_post_sueldo_empty():
    req_args = {"jugadores": []}
    response = client.post(
        "/api/sueldo/", headers={"Content-type": "application/json"}, json=req_args
    )
    assert response.status_code == 200
    assert {"jugadores": []} == response.json()
