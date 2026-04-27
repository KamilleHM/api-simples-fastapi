from fastapi.testclient import TestClient
from main import app

def test_sum_numbers():
    client = TestClient(app)
    response = client.get("/sum?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_subtract_numbers():
    client = TestClient(app)
    # Caso normal
    response = client.get("/subtract?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

    # Resultado negativo
    response = client.get("/subtract?a=3&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": -2}

    # Input inválido
    response = client.get("/subtract?a=abc&b=1")
    assert response.status_code == 455
