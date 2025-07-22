# app/tests/test_routes.py

# import pytest
from fastapi.testclient import TestClient

from app.main import app


def test_create_application():
    with TestClient(app) as client:
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
            "notes": "Initial application for backend role.",
        }
    response = client.post("/applications/", json=payload)
    assert response.status_code == 200
    assert response.json()["position_name"] == "Backend Developer"
    assert response.json()["application_status"] == "applied"
    assert response.json()["followed_up_status"] is False
    assert response.json()["interviewed_status"] is False
    assert response.json()["resume_link"] == "https://example.com/resume.pdf"

    print("RESPONSE JSON:", response.json())


def test_search_application_by_company_name():
    with TestClient(app) as client:
        payload = {
            "user_id": 5,
            "company_name": "SearchCorp",
            "position_name": "Full Stack Developer",
            "application_status": "applied",
            "application_date": "2025-07-21",
            "application_deadline": "2025-08-01",
            "followed_up_status": True,
            "interviewed_status": False,
            "resume_link": "https://example.com/fullstack_resume.pdf",
            "notes": "Excited about the tech stack.",
        }
        create_response = client.post("/applications/", json=payload)
        assert create_response.status_code == 200
        assert create_response.json()["company_name"] == "SearchCorp"

        search_response = client.get("/applications/search", params={"company_name": "SearchCorp"})
        assert search_response.status_code == 200
        assert isinstance(search_response.json(), list)
        assert any(app["company_name"] == "SearchCorp" for app in search_response.json())


def test_get_all_applications():
    # Make sure at least one exists
    with TestClient(app) as client:
        payload = {
            "user_id": 3,
            "company_name": "AllCorp",
            "position_name": "Frontend Dev",
            "application_status": "applied",
            "application_date": "2025-07-05",
            "followed_up_status": False,
            "interviewed_status": False,
            "resume_link": "https://example.com/frontend.pdf",
            "notes": "Fresh submission.",
        }
    client.post("/applications/", json=payload)

    response = client.get("/applications/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(app["company_name"] == "AllCorp" for app in response.json())


def test_delete_application():
    with TestClient(app) as client:
        payload = {
            "user_id": 4,
            "company_name": "DeleteCorp",
            "position_name": "QA Engineer",
            "application_status": "rejected",
            "application_date": "2025-07-01",
            "followed_up_status": False,
            "interviewed_status": False,
            "resume_link": "https://example.com/qa.pdf",
            "notes": "Position not filled.",
        }
    response = client.post("/applications/", json=payload)
    app_id = response.json()["application_id"]

    delete_response = client.delete(f"/applications/{app_id}")
    assert delete_response.status_code == 200 or delete_response.status_code == 204

    follow_up = client.get(f"/applications/{app_id}")
    assert follow_up.status_code == 404
