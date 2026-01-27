"""
API DE TESIS UNAP - SESION 3
Con PostgreSQL y SQLAlchemy

Ejecutar: uvicorn app.main:app --reload
Docs: http://localhost:8000/docs

Curso: Desarrollo de Software
Docente: Milton Vladimir Mamani Calisaya
Universidad Nacional del Altiplano - Puno
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import tesis
from app.database import init_db

# Crear aplicacion
app = FastAPI(
    title="API de Tesis UNAP",
    description="""
    API REST con PostgreSQL y SQLAlchemy.

    ## Sesion 3: Bases de Datos

    Ahora los datos persisten en PostgreSQL.
    """,
    version="2.0.0"
)

# CORS para permitir conexion desde React (localhost:5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174", "http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas al iniciar
@app.on_event("startup")
def startup():
    """Se ejecuta al iniciar la aplicacion"""
    init_db()
    print("Tablas creadas/verificadas en PostgreSQL")

# Registrar rutas
app.include_router(tesis.router)


@app.get("/", tags=["Inicio"])
def inicio():
    return {
        "mensaje": "API de Tesis UNAP v2.0",
        "docs": "/docs",
        "base_de_datos": "PostgreSQL + SQLAlchemy",
        "sesion": 3
    }


@app.get("/api/health", tags=["Utilidades"])
def health():
    return {"status": "ok", "database": "postgresql"}
