from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#URL para base de datos SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

#configuración del engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

#crea la sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base declarativa para modelos
Base = declarative_base()
