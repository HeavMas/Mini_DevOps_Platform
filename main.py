## gpt gen code
from fastapi import FastAPI, HTTPException
from typing import List
from models import Task

app = FastAPI()

# Временное хранилище (вместо БД)
tasks: List[Task] = []

# --- Healthcheck ---
@app.get("/health")
def health():
    return {"status": "ok"}

# --- Получить все задачи ---
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# --- Создать задачу ---
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

# --- Получить задачу ---
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# --- Обновить ---
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# --- Удалить ---
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            return {"message": "deleted"}
    raise HTTPException(status_code=404, detail="Task not found")