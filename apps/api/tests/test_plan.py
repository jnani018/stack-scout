from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_plan():
    resp = client.post("/v1/plan", json={"prompt":"Build a RAG app", "constraints":{"no_card":True}})
    assert resp.status_code == 200
    data = resp.json()
    assert "items" in data and len(data["items"]) >= 3
    assert data["totals"]["monthly"] == 0
