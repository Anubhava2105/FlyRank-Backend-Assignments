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
        