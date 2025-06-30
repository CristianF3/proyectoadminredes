from sqlalchemy.orm import Session
from app import models, schemas

#funcion para obtener un usuario por su id
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

#funcion para obtener todos los usuario
def get_users(db: Session):
    return db.query(models.User).all()

#funcion para obtener un usuario por su email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

#funcion para crear un usuario 
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
