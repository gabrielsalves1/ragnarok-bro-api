FROM python:3.10.0-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY . .

RUN apt-get update -y && \
    apt-get install libpq-dev python3-dev gcc -y && \
    pip install --upgrade pip && \
    pip install poetry && \
    poetry install

EXPOSE 8000
CMD [ "poetry", "run", "python3", "-u", "./app/main.py" ]