from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from app.database import Base
import enum

#Enum para estados válidos
class TaskStatus(str, enum.Enum):
    pendiente = "pendiente"
    en_progreso = "en_progreso"
    completada = "completada"

#estructura de la base de datos
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.pendiente, nullable=False)
    user_id = Column(Integer, nullable=False)  # Se validará contra el user-service
