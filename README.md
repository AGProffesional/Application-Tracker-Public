# Application Tracking Tool
A backend portfolio project built with Python using FastAPI, PostgreSQL, and Docker, designed to help users manage job applications effectively. This project showcases RESTful API design, containerized deployment, and CI/CD integration using GitHub Actions.

## Features
- Create update and delete job applications
- Filter by company, job position, application status, the date range of when the application was submitted, the application deadline, whether you've followed up, and whether you've interviwed.
- Auto-generated Swagger docs
- Dockerized for easy setup
- Secure environment configuration using a .env file
- CI/CD pipeline with testing and linting using Github Actions


## Tech Stack
|Technology    |Purpose                    |
|--------------|---------------------------|
|FastAPI       |Backend framework          |
|PostgreSQL    |Relational database        |
|Docker        |Containerization           |
|Docker Compose|Multi-service orchestration|
|GitHub Actions|CI/CD pipeline             |
|Pydantic      |Data Validation            |

## Setup Instructions
1. 
```
For windows users:
- run Start.bat to start the server

For mac/linux users:
- run Start.sh to start the server
```
2. Access the app
- Swagger UI: http://localhost:8000/docs

## Testing 
(For advanced users that are interested)
To run tests inside the container:
```bash
docker-compose exec app pytest
```

## Project Structure
<pre>
APPLICATION-TRACKER/
├── app/
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_routes.py
│   ├── __init__.py
│   ├── database.py
│   ├── extensions.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── utils.py
├── .dockerignore
├── .env.example
├── .flake8
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── README.md
├── requirements-dev.txt
</pre>

## License
MIT License