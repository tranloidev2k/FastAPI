from task_module.model import Task
from fastapi import APIRouter
from task_module.service import TaskService
from fastapi.params import Depends
router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/{id}")
def get_task_by_id(id: int, service: TaskService = Depends()):
    return service.get_by_id(id)

@router.post("", status_code=201)
def create_task(body: Task, service: TaskService = Depends()):
    return service.create_task(body)

@router.put("/{id}")
def update_task(id: int, body: Task, service: TaskService = Depends()):
    return service.update_task(id, body)

@router.delete("/{id}")
def delete_task(id: int, service: TaskService = Depends()):
    return service.delete_task(id)

@router.get("")
def get_all(service: TaskService = Depends()):
    return service.get_all()