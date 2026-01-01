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


def test_create_item(client: TestClient):
    token = get_auth_token(client)
    
    response = client.post(
        "/api/v1/items/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Test Item",
            "description": "Test Description"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Item"
    assert data["description"] == "Test Description"
    assert "id" in data


def test_read_items(client: TestClient):
    token = get_auth_token(client)
    
    client.post(
        "/api/v1/items/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Test Item 1",
            "description": "Test Description 1"
        }
    )
    
    response = client.get(
        "/api/v1/items/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_update_item(client: TestClient):
    token = get_auth_token(client)
    
    create_response = client.post(
        "/api/v1/items/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Test Item",
            "description": "Test Description"
        }
    )
    item_id = create_response.json()["id"]
    
    response = client.put(
        f"/api/v1/items/{item_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Updated Item"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Item"


def test_delete_item(client: TestClient):
    token = get_auth_token(client)
    
    create_response = client.post(
        "/api/v1/items/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Test Item",
            "description": "Test Description"
        }
    )
    item_id = create_response.json()["id"]
    
    response = client.delete(
        f"/api/v1/items/{item_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    
    get_response = client.get(
        f"/api/v1/items/{item_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert get_response.status_code == 404
