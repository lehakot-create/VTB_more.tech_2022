from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_post_role():
    url = "http://127.0.0.1:8000/role/"
    data = {"role": "buh"}
    response = client.request('POST', url=url, data=data)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
