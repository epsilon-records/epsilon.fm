# Third-Party Dependencies
from fastapi.testclient import TestClient

# Local Dependencies
from src.core.config import settings
from tests.helper import _get_token

# Test data: admin/superuser 'test' credentials
ADMIN_USERNAME = settings.ADMIN_USERNAME
ADMIN_PASSWORD = settings.ADMIN_PASSWORD

# Test global variables
test_default_tier_id = None
test_tier_id = None
test_tier = {"name": "Test Tier"}


def test_get_default_tier(client: TestClient) -> None:
    global test_default_tier_id
    assert test_default_tier_id is None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/system/tiers",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    tiers_data = response.json()["data"]

    # Create a dictionary to map tier names to IDs
    tiers_map = dict((tier["name"], tier["id"]) for tier in tiers_data)

    # Get the ID of the related tier using the mapping
    test_default_tier_id = tiers_map.get(settings.TIER_NAME_DEFAULT)

    assert response.status_code == 200
    assert test_default_tier_id is not None


def test_post_tier(client: TestClient) -> None:
    global test_tier_id
    assert test_tier_id is None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.post(
        "/api/v1/system/tiers",
        json=test_tier,
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    test_tier_id = response.json()["id"]

    assert response.status_code == 201
    assert test_tier_id is not None


def test_get_multiple_tiers(client: TestClient) -> None:
    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/system/tiers",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200
    assert len(response.json()["data"]) > 0


def test_get_tier(client: TestClient) -> None:
    global test_tier_id
    assert test_tier_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/system/tiers/{test_tier_id}",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200
    assert response.json()["name"] == test_tier["name"]


def test_update_tier(client: TestClient) -> None:
    global test_tier_id
    assert test_tier_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    updated_tier_name = "Updated Test Tier"

    response = client.patch(
        url=f"/api/v1/system/tiers/{test_tier_id}",
        json={"name": updated_tier_name},
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Tier updated"}


def test_update_tier_to_default(client: TestClient) -> None:
    global test_tier_id
    assert test_tier_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.patch(
        url=f"/api/v1/system/tiers/{test_tier_id}",
        json={"default": True},
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Extra inputs are not permitted"


def test_update_default_tier(client: TestClient) -> None:
    global test_default_tier_id
    assert test_default_tier_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    updated_default_tier_name = "Updated Default Tier"

    response = client.patch(
        url=f"/api/v1/system/tiers/{test_default_tier_id}",
        json={"name": updated_default_tier_name},
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 403
    assert response.json() == {"detail": "Default Tier cannot be updated"}


def test_delete_tier(client: TestClient) -> None:
    global test_tier_id
    assert test_tier_id is not None

    # Obter token de autenticação
    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.delete(
        url=f"/api/v1/system/tiers/{test_tier_id}",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Tier deleted"}


def test_delete_default_tier(client: TestClient) -> None:
    global test_default_tier_id
    assert test_default_tier_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.delete(
        url=f"/api/v1/system/tiers/{test_default_tier_id}",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 403
    assert response.json() == {"detail": "Default Tier cannot be deleted"}
