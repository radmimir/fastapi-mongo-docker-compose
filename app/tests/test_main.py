from starlette.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_get_employees():
    response = client.get("/employees")
    assert response.status_code == 200