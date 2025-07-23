#!/bin/bash
cd application-tracker
cp .env.example .env
docker-compose up --build