import pytest # type: ignore
from fastapi.testclient import TestClient # type: ignore
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_read_main(client):
    response = client.get("/api/v1")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
