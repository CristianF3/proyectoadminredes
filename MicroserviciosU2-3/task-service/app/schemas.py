from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    pendiente = "pendiente"
    en_progreso = "en_progreso"
    completada = "completada"

# Esquema base (opcional si quieres extender luego)
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: int

# Para crear una tarea
class TaskCreate(TaskBase):
    pass

# Para actualizar estado de una tarea
class TaskUpdate(BaseModel):
    status: TaskStatus

# Para devolver tareas completas desde la API
class Task(TaskBase):
    id: int
    status: TaskStatus

    class Config:
        orm_mode = True
