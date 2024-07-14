# Third-Party Dependencies
from fastapi.testclient import TestClient

# Local Dependencies
from src.core.config import settings
from tests.helper import _get_token

# Test data: admin/superuser 'test' credentials
ADMIN_USERNAME = settings.ADMIN_USERNAME
ADMIN_PASSWORD = settings.ADMIN_PASSWORD

# Test global variables
test_post_user_id = None
test_post_id = None
test_post = {
    "title": "This is my test post",
    "text": "This is the content of my test post.",
    "media_url": "https://www.imageurl.com/test_post.jpg",
}


def test_get_post_user_data(client: TestClient) -> None:
    global test_post_user_id
    assert test_post_user_id is None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/admin/users/me/",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    test_post_user_id = response.json()["id"]

    assert response.status_code == 200
    assert test_post_user_id is not None
    assert response.json()["username"] == ADMIN_USERNAME


def test_create_post(client: TestClient) -> None:
    global test_post_id
    global test_post_user_id
    assert test_post_id is None
    assert test_post_user_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.post(
        url=f"/api/v1/blog/posts/user/{test_post_user_id}",
        json=test_post,
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    test_post_id = response.json()["id"]

    assert response.status_code == 201
    assert test_post_id is not None


def test_get_created_post(client: TestClient) -> None:
    global test_post_id
    global test_post_user_id
    assert test_post_id is not None
    assert test_post_user_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/blog/posts/{test_post_id}/user/{test_post_user_id}",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    post = response.json()

    assert response.status_code == 200
    assert post["title"] == test_post["title"]
    assert post["text"] == test_post["text"]
    assert post["media_url"] == test_post["media_url"]


def test_get_multiple_user_posts(client: TestClient) -> None:
    global test_post_user_id
    assert test_post_user_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.get(
        url=f"/api/v1/blog/posts/user/{test_post_user_id}",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200
    assert len(response.json()["data"]) > 0


def test_update_post(client: TestClient) -> None:
    global test_post_id
    global test_post_user_id
    assert test_post_id is not None
    assert test_post_user_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.patch(
        url=f"/api/v1/blog/posts/{test_post_id}/user/{test_post_user_id}",
        json=test_post,
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Post updated"}


def test_delete_post(client: TestClient) -> None:
    global test_post_id
    global test_post_user_id
    assert test_post_id is not None
    assert test_post_user_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.delete(
        url=f"/api/v1/blog/posts/{test_post_id}/user/{test_post_user_id}",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Post deleted"}


def test_delete_already_deleted_post_as_admin(client: TestClient) -> None:
    global test_post_id
    global test_post_user_id
    assert test_post_id is not None
    assert test_post_user_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.delete(
        url=f"/api/v1/blog/posts/{test_post_id}/user/{test_post_user_id}",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Post already deleted (soft delete)."}


def test_delete_db_post(client: TestClient) -> None:
    global test_post_id
    global test_post_user_id
    assert test_post_id is not None
    assert test_post_user_id is not None

    token = _get_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, client=client)

    response = client.delete(
        url=f"/api/v1/blog/posts/{test_post_id}/user/{test_post_user_id}/db",
        headers={"Authorization": f'Bearer {token.json()["access_token"]}'},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Post deleted from the database"}
