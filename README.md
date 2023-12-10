# DOCS

Go to /docs to see documentation.

# SETUP

## Dependencies

Chrome + ChromeDriver
Python 3.10
Docker

## Running in a docker container

- docker-compose up -d

## Running local

1. Clone project

- git clone git@github.com:gabrielsalves1/ragnarok-bro-api.git

2. Install dependencies

apt:

- sudo apt install python3-dev libpq-dev gcc

pip and poetry commands:

- pip install poetry

- poetry shell

- poetry install

3. Run migrations

- cd app

- alembic upgrade head

# Execute app

- python3 app/main.py

# Execute scraping

- python3 web_scraping/main.py
