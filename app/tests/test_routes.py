# app/tests/test_routes.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_application():
    payload = {
    "user_id": 1,
    "company_name": "TestCorp",
    "position_name": "Backend Developer",
    "application_status": "applied",
    "application_date": "2025-07-16",
    "application_deadline": "2025-07-30",  # optional, but added for coverage
    "followed_up_status": False,
    "interviewed_status": False,
    "resume_link": "https://example.com/resume.pdf",
    "notes": "Initial application for backend role."
}
    response = client.post("/applications/", json=payload)
    assert response.status_code == 200
    assert response.json()["company"] == "TestCorp"
