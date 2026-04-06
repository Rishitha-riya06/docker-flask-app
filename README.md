# My First Docker App

A Flask web application containerized with Docker.

## What it does
- Serves a webpage at http://localhost:5000
- Returns JSON status at http://localhost:5000/status

## How to run

### Build the image
docker build -t rishitha-app:v1 .

### Run the container
docker run -d -p 5000:5000 --name my-flask-app rishitha-app:v1

### Stop the container
docker stop my-flask-app

## Tech stack
- Python 3.11
- Flask
- Docker

## Author
Rishitha — CSE Cybersecurity Student | DevOps Engineer in training
