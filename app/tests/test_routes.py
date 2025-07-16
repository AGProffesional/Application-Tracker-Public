# app/tests/test_routes.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_application():
    payload = {
        "company": "TestCorp",
        "position": "Backend Developer",
        "status": "applied"
    }
    response = client.post("/applications/", json=payload)
    assert response.status_code == 200
    assert response.json()["company"] == "TestCorp"
