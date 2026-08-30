from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")

# In-memory task storage
tasks = [
    {"id": 1, "title": "Write project plan", "done": False},
    {"id": 2, "title": "Review assignment requirements", "done": True},
]


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    done: bool = False


class Task(TaskCreate):
    id: int


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API!"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    new_task = {
        "id": max((existing_task["id"] for existing_task in tasks), default=0) + 1,
        "title": task.title,
        "done": task.done,
    }
    tasks.append(new_task)
    return new_task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate):
    for existing_task in tasks:
        if existing_task["id"] == task_id:
            existing_task["title"] = task.title
            existing_task["done"] = task.done
            return existing_task
    raise HTTPException(status_code=404, detail="Task not found")
