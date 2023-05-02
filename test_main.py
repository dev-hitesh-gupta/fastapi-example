from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    user = {"name": "John Doe", "email": "john.doe@example.com", "password": "password123"}
    response = client.post("/users", json=user)
    assert response.status_code == 200
    assert response.json()["name"] == user["name"]
    assert response.json()["email"] == user["email"]


def test_get_user():
    user = {"name": "John Doe", "email": "john.doe@example.com", "password": "password123"}
    response = client.post("/users", json=user)
    user_id = response.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == user["name"]
    assert response.json()["email"] == user["email"]


def test_update_user():
    user = {"name": "John Doe", "email": "john.doe@example.com", "password": "password123"}
    response = client.post("/users", json=user)
    user_id = response.json()["id"]
    updated_user = {"name": "Jane Doe", "email": "jane.doe@example.com", "password": "newpassword"}
    response = client.put(f"/users/{user_id}", json=updated_user)
    assert response.status_code == 200


def test_delete_user():
    user = {"name": "John Doe", "email": "john.doe@example.com", "password": "password123"}
    response = client.post("/users", json=user)
    user_id = response.json()["id"]
    print(user_id)
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
