#!/bin/bash
git clone https://github.com/testrepo
cd application-tracker
cp .env.example .env
docker-compose up --build