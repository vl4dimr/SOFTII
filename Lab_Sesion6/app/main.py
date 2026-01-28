"""
API DE TESIS UNAP - SESION 6
Aplicacion Completa: JWT + CRUD + DOCX + React + Tailwind

Ejecutar: uvicorn app.main:app --reload
Docs: http://localhost:8000/docs

Curso: Desarrollo de Software
Docente: Milton Vladimir Mamani Calisaya
Universidad Nacional del Altiplano - Puno
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, tesis, documentos
from app.database import init_db

# Crear aplicacion
app = FastAPI(
    title="API de Tesis UNAP",
    description="""
    API REST completa con JWT + CRUD + Generacion DOCX.

    ## Sesion 6: Aplicacion Completa

    - Autenticacion JWT (registro, login, proteccion de endpoints)
    - CRUD de tesis con PostgreSQL
    - Generacion de documentos DOCX con formato UNAP
    - Frontend React + Tailwind CSS
    """,
    version="6.0.0"
)

# Configurar CORS para el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://localhost:5173",
        "http://localhost:3000",
    ],
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
app.include_router(auth.router)
app.include_router(tesis.router)
app.include_router(documentos.router)


@app.get("/", tags=["Inicio"])
def inicio():
    return {
        "mensaje": "API de Tesis UNAP v6.0 - Aplicacion Completa",
        "docs": "/docs",
        "endpoints": {
            "auth": {
                "register": "POST /auth/register",
                "login": "POST /auth/login",
                "perfil": "GET /auth/me (requiere token)"
            },
            "tesis": "/api/tesis (requiere token)",
            "documentos": "/documentos/tesis/{id}/docx (requiere token)"
        },
        "sesion": 6
    }


@app.get("/api/health", tags=["Utilidades"])
def health():
    return {"status": "ok", "database": "postgresql", "auth": "jwt", "docx": "python-docx"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
