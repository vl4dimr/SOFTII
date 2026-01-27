"""
API DE TESIS UNAP - SESION 5
Generacion de Documentos DOCX

Ejecutar: uvicorn app.main:app --reload
Docs: http://localhost:8000/docs

Curso: Desarrollo de Software
Docente: Milton Vladimir Mamani Calisaya
Universidad Nacional del Altiplano - Puno
"""

from fastapi import FastAPI
from app.routes import tesis
from app.routes import documentos
from app.database import init_db

# Crear aplicacion
app = FastAPI(
    title="API de Tesis UNAP",
    description="""
    API REST con generacion de documentos DOCX.

    ## Sesion 5: Generacion de Documentos

    Genera documentos Word con formato UNAP desde los datos de tesis.
    """,
    version="5.0.0"
)

# Crear tablas al iniciar
@app.on_event("startup")
def startup():
    """Se ejecuta al iniciar la aplicacion"""
    init_db()
    print("Tablas creadas/verificadas en PostgreSQL")

# Registrar rutas
app.include_router(tesis.router)
app.include_router(documentos.router)


@app.get("/", tags=["Inicio"])
def inicio():
    return {
        "mensaje": "API de Tesis UNAP v5.0 - Generacion DOCX",
        "docs": "/docs",
        "base_de_datos": "PostgreSQL + SQLAlchemy",
        "endpoints": {
            "tesis": "/api/tesis",
            "documentos": "/documentos/tesis/{id}/docx",
            "preview": "/documentos/tesis/{id}/preview"
        },
        "sesion": 5
    }


@app.get("/api/health", tags=["Utilidades"])
def health():
    return {"status": "ok", "database": "postgresql", "docx": "python-docx"}
