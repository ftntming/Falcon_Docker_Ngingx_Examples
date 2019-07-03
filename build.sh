#!/bin/bash -e
docker network create backend-network || true
docker build -t falconbase falconbase --network=host
docker-compose up --build --scale falcontest=3
