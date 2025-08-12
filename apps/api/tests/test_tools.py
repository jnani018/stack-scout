from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_tools():
    r = client.get("/v1/tools")
    assert r.status_code == 200
    data = r.json()
    assert data["count"] >= 5
