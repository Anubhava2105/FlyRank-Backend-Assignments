from fastapi import FastAPI, HTTPException
tasks=[
    {"id":1,"title":"Watch lecture","done":False},
    {"id":2,"title":"Do assignment","done":True},
    {"id":3,"title":"Wash dishes","done":True}
]


app=FastAPI();

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
        
@app.post("/tasks")

def create_task(title:str):
    if(title is None):
        raise HTTPException(status_code=400,detail="Title is required")
    max=0
    for t in tasks:
        if t["id"]>max:
            max=t["id"]
    new_task={"id":max+1,"title":title,"done":False}
    tasks.append(new_task)
    raise HTTPException(status_code=201,detail="Task created successfully") 
    return new_task

