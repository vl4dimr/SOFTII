"""
CONEXION A LA BASE DE DATOS
SQLAlchemy + PostgreSQL

Sesion 4: Autenticacion JWT
Curso: Desarrollo de Software - UNAP
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# URL de conexion desde .env
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:admin@localhost:5432/qillqay"
)

# Motor de conexion
engine = create_engine(DATABASE_URL)

# Fabrica de sesiones
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para modelos
Base = declarative_base()


def get_db():
    """
    Dependency para FastAPI.
    Crea una sesion por request y la cierra al terminar.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    Crea todas las tablas en la base de datos.
    """
    Base.metadata.create_all(bind=engine)
