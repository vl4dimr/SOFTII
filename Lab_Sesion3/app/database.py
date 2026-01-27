"""
CONEXION A LA BASE DE DATOS
SQLAlchemy + PostgreSQL

Sesion 3: Bases de Datos
Curso: Desarrollo de Software - UNAP
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# URL de conexión desde .env
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:123456@localhost/qillqay"
)

# Motor de conexión
engine = create_engine(DATABASE_URL)

# Fábrica de sesiones
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
    Crea una sesión por request y la cierra al terminar.
    
    Uso:
        @router.get("/")
        def endpoint(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    Crea todas las tablas en la base de datos.
    Llamar una vez al iniciar la aplicación.
    """
    Base.metadata.create_all(bind=engine)
