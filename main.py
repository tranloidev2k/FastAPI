from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from task_module.controller import router as task_router

app = FastAPI()
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/users")
def get_users(limit: int = 10):
    return {"limit": limit}

app.include_router(task_router)
