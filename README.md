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
1. Clone the repository
```bash
git clone https://github.com/testrepo
cd application-tracker
```

2. Set up Environment Variables
```bash
cp .env.example .env
#Make sure to keep the DBHost and DBPort since the database is dockerized.
#Fill in your own DBUser, DBPass, and DBName
``` 

3. Run with Docker Compose
```bash
docker-compose up --build
```

4. Access the app
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs

## Testing
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