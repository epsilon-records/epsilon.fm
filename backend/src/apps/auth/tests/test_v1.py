# Third-Party Dependencies
from sqlalchemy.ext.asyncio import AsyncEngine
from fastapi.testclient import TestClient
from sqlalchemy.future import select

# Local Dependencies
from src.core.config import settings

# Test data: admin/superuser 'test' credentials
ADMIN_USERNAME = settings.ADMIN_USERNAME
ADMIN_PASSWORD = settings.ADMIN_PASSWORD

# Test global variables
test_access_token = None
test_refresh_token_cookie = None


def test_auth_login(client: TestClient) -> None:
    global test_access_token
    global test_refresh_token_cookie

    response = client.post(
        "/api/v1/system/auth/login",
        data={"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD},
        headers={"content-type": "application/x-www-form-urlencoded"},
    )

    response_json = response.json()
    test_access_token = response_json["access_token"]
    test_token_type = response_json["token_type"]
    test_refresh_token_cookie = response.cookies.get("refresh_token")

    assert response.status_code == 200
    assert test_access_token is not None
    assert test_token_type == "bearer"


def test_auth_refresh(client: TestClient) -> None:
    client.cookies.update({"refresh_token": test_refresh_token_cookie})

    response = client.post("/api/v1/system/auth/refresh")

    response_json = response.json()
    new_access_token = response_json["access_token"]
    token_type = response_json["token_type"]

    assert response.status_code == 200
    assert new_access_token is not None
    assert token_type == "bearer"


def test_auth_logout(client: TestClient) -> None:
    response_logout = client.post(
        "/api/v1/system/auth/logout",
        headers={"Authorization": f"Bearer {test_access_token}"},
    )

    response_json_logout = response_logout.json()

    assert response_logout.status_code == 200
    assert response_json_logout == {"message": "Logged out successfully"}
    assert "refresh_token" not in response_logout.cookies
