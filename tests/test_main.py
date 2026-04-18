from fastapi.testclient import TestClient
from main import app

def test_sum_numbers():
    client = TestClient(app)
    response = client.get("/sum?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}
