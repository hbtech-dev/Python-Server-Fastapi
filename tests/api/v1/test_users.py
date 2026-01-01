from fastapi.testclient import TestClient


def get_auth_token(client: TestClient) -> str:
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword123",
            "full_name": "Test User"
        }
    )
    
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "test@example.com",
            "password": "testpassword123"
        }
    )
    return response.json()["access_token"]


def test_read_user_me(client: TestClient):
    token = get_auth_token(client)
    
    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["username"] == "testuser"


def test_update_user_me(client: TestClient):
    token = get_auth_token(client)
    
    response = client.put(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "full_name": "Updated Name"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["full_name"] == "Updated Name"


def test_read_users_unauthorized(client: TestClient):
    response = client.get("/api/v1/users/me")
    assert response.status_code == 401
