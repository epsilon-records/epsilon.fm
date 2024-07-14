# Built-in Dependencies
from uuid import uuid4

# Third-Party Dependencies
from fastapi.testclient import TestClient

# Local Dependencies
from src.core.utils.rate_limit import sanitize_path
from src.core.config import settings
from tests.helper import _get_token

# Test data: admin/superuser 'test' credentials
ADMIN_USERNAME = settings.ADMIN_USERNAME
ADMIN_PASSWORD = settings.ADMIN_PASSWORD

# Test global variables
test_related_tier_id = None
test_rate_limit_id = None
test_rate_limit = {
    "name": "Test Rate Limit",
    "path": "/api/v1/admin/tasks",
    "limit": 100,
    "period": 3600,
}


def test_get_related_tier_data(client: TestClient) -> None:
    global test_related_tier_id
    assert test_related_tier_id is None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/system/tiers",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    tiers_data = response.json()["data"]

    # Create a dictionary to map tier names to IDs
    tiers_map = dict((tier["name"], tier["id"]) for tier in tiers_data)

    # Get the ID of the related tier using the mapping
    test_related_tier_id = tiers_map.get(settings.TIER_NAME_DEFAULT)

    assert response.status_code == 200
    assert test_related_tier_id is not None


def test_post_rate_limit(client: TestClient) -> None:
    global test_related_tier_id
    global test_rate_limit_id
    assert test_related_tier_id is not None
    assert test_rate_limit_id is None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.post(
        url=f"/api/v1/system/rate-limits/tier/{test_related_tier_id}",
        json=test_rate_limit,
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )
    test_rate_limit_id = response.json()["id"]

    assert response.status_code == 201
    assert test_rate_limit_id is not None


def test_post_invalid_rate_limit_related_tier_id(client: TestClient) -> None:
    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    invalid_related_tier_id = f"{uuid4()}"

    response = client.post(
        url=f"/api/v1/system/rate-limits/tier/{invalid_related_tier_id}",
        json=test_rate_limit,
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 404


def test_post_invalid_rate_limit_path(client: TestClient) -> None:
    global test_related_tier_id
    assert test_related_tier_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    invalid_test_rate_limit = test_rate_limit.copy()
    invalid_test_rate_limit["path"] = "/api/v1/invalid/route"

    response = client.post(
        url=f"/api/v1/system/rate-limits/tier/{test_related_tier_id}",
        json=invalid_test_rate_limit,
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 422


def test_get_multiple_rate_limits(client: TestClient) -> None:
    global test_related_tier_id
    assert test_related_tier_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/system/rate-limits/tier/{test_related_tier_id}",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200
    assert "data" in response.json()


def test_get_rate_limit(client: TestClient) -> None:
    global test_related_tier_id
    global test_rate_limit_id
    assert test_related_tier_id is not None
    assert test_rate_limit_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/system/rate-limits/{test_rate_limit_id}/tier/{test_related_tier_id}",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    rate_limit = response.json()

    assert response.status_code == 200
    assert rate_limit["name"] == test_rate_limit["name"]
    assert rate_limit["path"] == sanitize_path(test_rate_limit["path"])
    assert rate_limit["limit"] == test_rate_limit["limit"]
    assert rate_limit["period"] == test_rate_limit["period"]


def test_update_rate_limit(client: TestClient) -> None:
    global test_related_tier_id
    global test_rate_limit_id
    assert test_related_tier_id is not None
    assert test_rate_limit_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    updated_rate_limit = {
        "name": "Updated Test Rate Limit",
        "limit": 200,
        "period": 7200,
    }

    response = client.patch(
        url=f"/api/v1/system/rate-limits/{test_rate_limit_id}/tier/{test_related_tier_id}",
        json=updated_rate_limit,
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Rate Limit updated"}


def test_erase_rate_limit(client: TestClient) -> None:
    global test_related_tier_id
    global test_rate_limit_id
    assert test_related_tier_id is not None
    assert test_rate_limit_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.delete(
        url=f"/api/v1/system/rate-limits/{test_rate_limit_id}/tier/{test_related_tier_id}",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Rate Limit deleted"}
