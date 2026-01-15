import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import User, Item
from sqlalchemy.orm import Session
from app.database import get_db, engine
from app.schemas import UserCreate, ItemCreate

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="module")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_create_user(test_client, db_session):
    user_data = {"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    response = test_client.post("/users/", json=user_data)
    assert response.status_code == 201
    assert response.json()["username"] == user_data["username"]

def test_create_item(test_client, db_session):
    user = User(username="testuser", email="test@example.com", hashed_password="hashedpassword")
    db_session.add(user)
    db_session.commit()
    item_data = {"name": "Test Item", "description": "This is a test item.", "owner_id": user.id}
    response = test_client.post("/items/", json=item_data)
    assert response.status_code == 201
    assert response.json()["name"] == item_data["name"]

def test_get_user(test_client):
    response = test_client.get("/users/testuser")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_get_item(test_client):
    response = test_client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

def test_create_user_invalid_email(test_client):
    user_data = {"username": "testuser2", "email": "invalidemail", "password": "testpassword"}
    response = test_client.post("/users/", json=user_data)
    assert response.status_code == 422

def test_create_item_invalid_owner(test_client):
    item_data = {"name": "Invalid Item", "description": "This item has an invalid owner.", "owner_id": 999}
    response = test_client.post("/items/", json=item_data)
    assert response.status_code == 404

def test_user_acceptance(test_client):
    response = test_client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_item_acceptance(test_client):
    response = test_client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)