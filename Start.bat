@echo off
git clone https://github.com/testrepo
cd application-tracker
copy .env.example .env
docker-compose up --build