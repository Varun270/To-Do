from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/api/tasks", json={
        "title": "Test Task",
        "description": "Test Desc"
    })
    assert response.status_code == 200
    assert "task_id" in response.json()

def test_get_tasks():
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
