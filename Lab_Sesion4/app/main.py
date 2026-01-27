"""
API DE TESIS UNAP - SESION 4
Autenticacion con JWT

Ejecutar: uvicorn app.main:app --reload
Docs: http://localhost:8000/docs

Curso: Desarrollo de Software
Docente: Milton Vladimir Mamani Calisaya
Universidad Nacional del Altiplano - Puno
"""

from fastapi import FastAPI
from app.routes import auth
from app.database import init_db

# Crear aplicacion
app = FastAPI(
    title="API de Tesis UNAP",
    description="""
    API REST con Autenticacion JWT.

    ## Sesion 4: Autenticacion

    Registro, Login y proteccion de endpoints con JWT.
    """,
    version="3.0.0"
)


# Crear tablas al iniciar
@app.on_event("startup")
def startup():
    """Se ejecuta al iniciar la aplicacion"""
    init_db()
    print("Tablas creadas/verificadas en PostgreSQL")


# Registrar rutas
app.include_router(auth.router)


@app.get("/", tags=["Inicio"])
def inicio():
    return {
        "mensaje": "API de Tesis UNAP v3.0 - Con JWT",
        "docs": "/docs",
        "endpoints": {
            "register": "POST /auth/register",
            "login": "POST /auth/login",
            "perfil": "GET /auth/me (requiere token)"
        },
        "sesion": 4
    }


@app.get("/api/health", tags=["Utilidades"])
def health():
    return {"status": "ok", "database": "postgresql", "auth": "jwt"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
