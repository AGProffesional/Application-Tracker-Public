@echo off
cd application-tracker
copy .env.example .env
docker-compose up --build