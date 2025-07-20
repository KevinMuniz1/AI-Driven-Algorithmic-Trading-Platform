from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Algorithmic Trading API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Backend is running"}



from celery_app import celery_app

@app.get("/hello/{name}")
def trigger_hello(name: str):
    task = celery_app.send_task("tasks.say_hello.say_hello", args=[name])
    return {"task_id": task.id}
