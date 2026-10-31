from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_hello_with_name():
    response = client.get("/hello?name=test")
    assert response.status_code == 200
    assert response.json()["message"] == "hello, test"