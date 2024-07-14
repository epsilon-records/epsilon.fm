# Third-Party Dependencies
from fastapi.testclient import TestClient

# Local Dependencies
from src.core.config import settings
from tests.helper import _get_token

# Test data: admin/superuser 'test' credentials
ADMIN_USERNAME = settings.ADMIN_USERNAME
ADMIN_PASSWORD = settings.ADMIN_PASSWORD

# Test global variables
test_task_id = None
test_task_message = "Test Message"


def test_create_task(client: TestClient) -> None:
    global test_task_id
    assert test_task_id is None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.post(
        url=f"/api/v1/admin/tasks?message={test_task_message}",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    test_task_id = response.json()["id"]

    assert response.status_code == 201
    assert test_task_id is not None


def test_get_task(client: TestClient) -> None:
    global test_task_id
    assert test_task_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/admin/tasks/{test_task_id}",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200
    assert response.json()["args"][0] == test_task_message


def test_read_processed_tasks(client: TestClient) -> None:
    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/admin/tasks/processed",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200


def test_read_pending_tasks(client: TestClient) -> None:
    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/admin/tasks/pending",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200


def test_get_health_check_from_inexistent_queue(client: TestClient) -> None:
    inexistent_queue_name = "inexistent_queue"

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/admin/tasks/queue-health/",
        params={"queue_name": f"{inexistent_queue_name}"},
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": f"Queue with name '{inexistent_queue_name}' not found on broker."
    }
