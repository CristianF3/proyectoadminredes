from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app import models, schemas, crud, database

models.Base.metadata.create_all(bind=database.engine)
#se agregar el prefijo /api
app = FastAPI(title="User Service", root_path="/api")

#dependencia para obtener una sesión de DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

#ruta de estado de la base de datos
@app.get("/tasks/health")
def health_check():
    return {"status": "ok"}

#ruta de post task
@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

#ruta de get tasks
@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(user_id: int = Query(None), db: Session = Depends(get_db)):
    if user_id is not None:
        return crud.get_tasks_by_user(db, user_id)
    return crud.get_tasks(db)

#ruta de get task especifica
@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

#ruta de put estado de task especifica
@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task_status(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.update_task_status(db, task_id, task_update.status)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
