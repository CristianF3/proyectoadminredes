from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL para base de datos SQLite (archivo local)
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

# Configuración del engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crea la sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para modelos
Base = declarative_base()
