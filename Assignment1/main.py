from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
tasks=[
    {"id":1,"title":"Watch lecture","done":False},
    {"id":2,"title":"Do assignment","done":True},
    {"id":3,"title":"Wash dishes","done":True}
]


app=FastAPI();

class TaskModel(BaseModel):
    id: int = None
    title: str
    done: bool = False

@app.get("/")
def read_root():
    return {"name": "Task API", "version":"1.0","endpoints":["/tasks"]}

@app.get("/health")
def get_health():
    return {"status":"ok"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task_by_id(id:int):
    task=[t for t in tasks if t["id"]==id]
    if task:
        return task[0]
    else:
        raise HTTPException(status_code=404, detail=f"Task {id} not found")
        
@app.post("/tasks", status_code=201)
def create_task(task:TaskModel):
    new_task = {"id": len(tasks) + 1, "title": task.title, "done": task.done}
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{id}", status_code=200)
def update_tasks(id: int, task: TaskModel):
    found_task = [t for t in tasks if t["id"]==id]
    if(not found_task):
        raise HTTPException(status_code=404,detail=f"Task {id} not found")
    if(task.title is not None):
        found_task[0]["title"]=task.title
    if(task.done is not None):
        found_task[0]["done"]=task.done
    return found_task[0]

@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int):
    found_task = [t for t in tasks if t["id"]==id]
    if(not found_task):
        raise HTTPException(status_code=404,detail=f"Task {id} not found")
    tasks.remove(found_task[0])