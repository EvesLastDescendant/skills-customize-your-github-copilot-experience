from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    title: str
    completed: bool = False


items = []


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Add CRUD endpoints for tasks here
