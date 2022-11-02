from fastapi.testclient import TestClient

from app.api.fapi import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert 200 == response.status_code


def test_hello_world():
    response = client.get("/api/sueldo")
    assert response.status_code == 200
    assert {} == response.json()
