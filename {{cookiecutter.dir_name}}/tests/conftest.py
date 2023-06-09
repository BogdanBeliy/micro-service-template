import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="session")
def client() -> TestClient:
    with TestClient(app) as client:
        yield client
