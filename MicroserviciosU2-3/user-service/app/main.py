from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Service", root_path="/api")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/health")
def health():
    return {"status": "ok"}

@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

@app.get("/users", response_model=list[schemas.UserOut])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/users/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
