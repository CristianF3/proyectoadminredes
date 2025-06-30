from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#URL para base de datos SQLite
DATABASE_URL = "sqlite:///./users.db"

#configuración del engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

#crea la sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base declarativa para modelos
Base = declarative_base()
    