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
    assert response.json()["position_name"] == "Backend Developer"
    assert response.json()["application_status"] == "applied"
    assert response.json()["followed_up_status"] is False
    assert response.json()["interviewed_status"] is False
    assert response.json()["resume_link"] == "https://example.com/resume.pdf"

    print("RESPONSE JSON:", response.json())

def test_get_single_application():
    payload = {
        "user_id": 2,
        "company_name": "FetchCorp",
        "position_name": "DevOps Engineer",
        "application_status": "interviewed",
        "application_date": "2025-07-10",
        "followed_up_status": True,
        "interviewed_status": True,
        "resume_link": "https://example.com/devops_resume.pdf",
        "notes": "Interview completed."
    }
    response = client.post("/applications/", json=payload)
    app_id = response.json()["application_id"]

    get_response = client.get(f"/applications/{app_id}")
    assert get_response.status_code == 200
    assert get_response.json()["position_name"] == "DevOps Engineer"

def test_get_all_applications():
    # Make sure at least one exists
    payload = {
        "user_id": 3,
        "company_name": "AllCorp",
        "position_name": "Frontend Dev",
        "application_status": "applied",
        "application_date": "2025-07-05",
        "followed_up_status": False,
        "interviewed_status": False,
        "resume_link": "https://example.com/frontend.pdf",
        "notes": "Fresh submission."
    }
    client.post("/applications/", json=payload)

    response = client.get("/applications/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(app["company_name"] == "AllCorp" for app in response.json())

def test_delete_application():
    payload = {
        "user_id": 4,
        "company_name": "DeleteCorp",
        "position_name": "QA Engineer",
        "application_status": "rejected",
        "application_date": "2025-07-01",
        "followed_up_status": False,
        "interviewed_status": False,
        "resume_link": "https://example.com/qa.pdf",
        "notes": "Position not filled."
    }
    response = client.post("/applications/", json=payload)
    app_id = response.json()["application_id"]

    delete_response = client.delete(f"/applications/{app_id}")
    assert delete_response.status_code == 200 or delete_response.status_code == 204

    follow_up = client.get(f"/applications/{app_id}")
    assert follow_up.status_code == 404
