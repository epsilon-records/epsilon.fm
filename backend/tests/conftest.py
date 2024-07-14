# Third-Party Dependencies
import pytest
from fastapi.testclient import TestClient

# Local Dependencies
from src.main import app


@pytest.fixture(scope="session")
def client():
    """
    Pytest fixture to provide a FastAPI TestClient instance for testing.

    This fixture sets up a TestClient instance using the main FastAPI app, and the scope is set to session,
    meaning it will be shared among all test functions in a session.

    Returns
    ----------
    TestClient
        The FastAPI TestClient instance.

    Example
    ----------
    Using the `client` fixture in a test function:
    ```python
    def test_example(client):
        response = client.get("/example")
        assert response.status_code == 200
        assert response.json() == {"message": "Example response"}
    ```
    """
    with TestClient(app) as _client:
        yield _client
