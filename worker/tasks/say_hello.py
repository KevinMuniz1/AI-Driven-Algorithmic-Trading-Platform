# worker/tasks/say_hello.py

from worker.celery_worker import celery_app

@celery_app.task
def say_hello(name: str):
    return f"Hello, {name}!"
