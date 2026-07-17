# syntax=docker/dockerfile:1
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/app

WORKDIR /app

# ---- deps stage: install dependencies only (no project build) ----
FROM base AS deps
COPY pyproject.toml ./
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir \
        fastapi[standard] \
        uvicorn[standard] \
        sqlalchemy[asyncio] \
        asyncpg \
        alembic \
        redis[hiredis] \
        celery[redis] \
        flower \
        httpx[http2] \
        pydantic \
        pydantic-settings \
        dependency-injector \
        structlog \
        pyseto \
        passlib[bcrypt] \
        prometheus-client \
        prometheus-fastapi-instrumentator \
        opentelemetry-sdk \
        opentelemetry-api \
        opentelemetry-exporter-otlp \
        opentelemetry-instrumentation-fastapi \
        opentelemetry-instrumentation-sqlalchemy \
        opentelemetry-instrumentation-httpx \
        opentelemetry-instrumentation-redis \
        opentelemetry-instrumentation-celery \
        langchain \
        langchain-community \
        langchain-ollama \
        orjson \
        tenacity \
        slowapi \
        python-dateutil \
        pytest \
        pytest-asyncio \
        pytest-cov \
        testcontainers[postgresql,redis] \
        respx \
        faker \
        hypothesis \
        ruff \
        mypy \
        bandit \
        safety \
        pre-commit

# ---- runtime stage: copy source + install project in editable mode ----
FROM deps AS runtime
COPY . .
RUN pip install ".[dev]" --no-deps
EXPOSE 8700
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8700"]
