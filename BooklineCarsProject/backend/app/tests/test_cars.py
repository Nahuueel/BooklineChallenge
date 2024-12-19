import pytest # type: ignore
from fastapi.testclient import TestClient # type: ignore
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test__get_available_cars__returns_200(client):
    response = client.get(
        "/api/v1/cars/available?specified_date=2008-10-11",
    )
    assert response.status_code == 200


def test__get_available_cars__returns_422(client):
    response = client.get(
        "/api/v1/cars/available?specified_date=BadFormar",
    )
    assert response.status_code == 422

def test__post_car_booking__returns_422(client):
    response = client.post(
        "/api/v1/cars/book_a_car?booking_date=BadFormat&car_name=IDontExist",
    )
    assert response.status_code == 422

def test__post_car_booking__returns_400(client):
    response = client.post(
        "/api/v1/cars/book_a_car?booking_date=2008-10-11&car_name=IDontExist",
    )
    assert response.status_code == 400

def test__post_car_booking__returns_200(client):
    response = client.post(
        "/api/v1/cars/book_a_car?booking_date=2008-12-19&car_name=Toyo 4x4",
    )
    assert response.status_code == 200
