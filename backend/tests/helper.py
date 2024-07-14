# Third-Party Dependencies
from fastapi.testclient import TestClient


def _get_token(username: str, password: str, client: TestClient):
    """
    Helper function to obtain an authentication token by making a login request to the authentication endpoint.

    Parameters
    ----------
    username : str
        The username for authentication.
    password : str
        The password for authentication.
    client : TestClient
        The FastAPI test client instance.

    Returns
    ----------
    response
        The response object containing the authentication token.

    Example
    ----------
    Obtaining an authentication token:
    ```python
    token_response = _get_token("example_user", "example_password", test_client_instance)
    ```
    """
    return client.post(
        "/api/v1/system/auth/login",
        data={"username": username, "password": password},
        headers={"content-type": "application/x-www-form-urlencoded"},
    )
