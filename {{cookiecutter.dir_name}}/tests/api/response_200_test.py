from starlette import status
from starlette.testclient import TestClient


def test__first(client: TestClient):
    response = client.get('/')

    assert response.status_code == status.HTTP_200_OK
