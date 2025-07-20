from celery import Celery

# Celery instance (used inside the worker container)
celery_app = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

# Import tasks (auto-discovered)
celery_app.autodiscover_tasks(["tasks"])
