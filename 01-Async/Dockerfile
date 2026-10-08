FROM python:3.12.8-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEPYTECODE=1

WORKDIR /app

RUN pip3 install --upgrade --no-cache-dir pip \
    && pip3 install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install --only main

COPY lwasync lwasync

ENV PORT=8080

CMD poetry run uvicorn lwasync.server:app --host 0.0.0.0 --port $PORT
