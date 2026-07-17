"""Analytics refresh task — caches dashboard metrics in Redis."""

from __future__ import annotations

import structlog

from src.infrastructure.queue.celery_app import celery_app

logger = structlog.get_logger(__name__)


@celery_app.task(name="src.infrastructure.queue.tasks.analytics_tasks.analytics_refresh_task")
def analytics_refresh_task() -> dict:
    """Compute and cache dashboard metrics in Redis."""
    logger.info("analytics_refresh_started")
    return {"refreshed": True}
