from task_module.model import Task
from task_module.repository import get_tasks_db
from fastapi import HTTPException, Depends
class TaskService:
    def __init__(self, tasks: list = Depends(get_tasks_db)):
        self.tasks = tasks

    def get_by_id(self, id: int):
        for task in self.tasks:
            if task.id == id:
                return task
        raise HTTPException(status_code=404, detail="Task not found")

    def create_task(self, body: Task):
        self.tasks.append(body)
        return body

    def update_task(self, id: int, body: Task):
        for task in self.tasks:
            if task.id == id:
                task.title = body.title
                task.done = body.done
                return task
        raise HTTPException(status_code=404, detail="Task not found")   

    def delete_task(self, id: int):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                return task
        raise HTTPException(status_code=404, detail="Task not found")

    def get_all(self):
        return self.tasks   