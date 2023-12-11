![alt text](./img/logo_ragnarok.png)

# DOCS

Go to /docs to see documentation.

# SETUP

## DEPENDENCIES

Chrome + ChromeDriver
Python 3.10
Docker

## RUNNING IN A DOCKER CONTAINER

This will start a container with app, postgres, pgadmin, selenium and a web scraping to populate database with informations in https://playragnarokonlinebr.com/database/thor. The web scraping will consult page a page and get data to send a request to app.

- docker-compose up -d

## RUNNING LOCAL

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

- poetry run alembic upgrade head

## EXECUTE APP

You will need a instance of postgres running.

- poetry run python3 app/main.py

## EXECUTE WEB SCRAPING

The web scraping will consult page a page and get data to send a request to app.

- poetry run python3 web_scraping/main.py
