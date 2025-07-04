from sqlalchemy.orm import Session
from app import models, schemas

#funcion para crear la task
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        user_id=task.user_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

#funcion para obtener todas las tasks de la bd
def get_tasks(db: Session):
    return db.query(models.Task).all()

#funcion para obtener una de las tasks de la bd segun id
def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

#funcion para obtener todas de las tasks de la bd de un usuario segun su id
def get_tasks_by_user(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.user_id == user_id).all()

#funcion para actualizar estado de tasks de la bd por su id
def update_task_status(db: Session, task_id: int, new_status: schemas.TaskStatus):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        task.status = new_status
        db.commit()
        db.refresh(task)
    return task
