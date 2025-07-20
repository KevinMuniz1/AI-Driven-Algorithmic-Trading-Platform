from celery import Celery

# Celery instance (used by FastAPI)
celery_app = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)
