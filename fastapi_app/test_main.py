from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    import uuid
    unique_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    
    response = client.post(
        "/users/",
        json={"name": "Test User", "email": unique_email},
    )
    assert response.status_code == 200
    assert response.json()["email"] == unique_email

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)