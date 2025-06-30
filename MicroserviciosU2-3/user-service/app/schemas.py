from pydantic import BaseModel, EmailStr

#esquema base
class UserBase(BaseModel):
    name: str
    email: EmailStr

#para crear un usuario
class UserCreate(UserBase):
    pass

#para mostrar un usuario
class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True
