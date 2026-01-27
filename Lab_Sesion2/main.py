"""
LABORATORIO MVC - SESIÓN 2
Curso: Desarrollo de Software
Docente: Milton Vladimir Mamani Calisaya
Universidad Nacional del Altiplano - Puno

Ejecutar con: python main.py
Documentación: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ═══════════════════════════════════════════════════════════════
# MODELO (Normalmente estaría en /models/tesis.py)
# ═══════════════════════════════════════════════════════════════

class Tesis:
    """Clase que representa una tesis"""
    
    def __init__(self, id: int, titulo: str, autor: str, escuela: str):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.escuela = escuela
        self.estado = "borrador"
        self.created_at = datetime.now()
    
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "escuela": self.escuela,
            "estado": self.estado,
            "created_at": self.created_at.isoformat()
        }


# ═══════════════════════════════════════════════════════════════
# BASE DE DATOS SIMULADA
# ═══════════════════════════════════════════════════════════════

class BaseDeDatos:
    def __init__(self):
        self.tesis = {}
        self.contador = 0
        self._cargar_datos_ejemplo()
    
    def _cargar_datos_ejemplo(self):
        ejemplos = [
            ("Análisis de algoritmos de ordenamiento en Python", "Juan Pérez", "Ing. Sistemas"),
            ("Machine Learning aplicado a la agricultura del Altiplano", "María García", "Ing. Sistemas"),
            ("Sistema web para gestión de biblioteca", "Carlos López", "Ing. Sistemas"),
        ]
        for titulo, autor, escuela in ejemplos:
            self.insertar(titulo, autor, escuela)
    
    def insertar(self, titulo: str, autor: str, escuela: str) -> Tesis:
        self.contador += 1
        nueva = Tesis(self.contador, titulo, autor, escuela)
        self.tesis[self.contador] = nueva
        return nueva
    
    def obtener_todos(self) -> list:
        return [t.to_dict() for t in self.tesis.values()]
    
    def obtener_por_id(self, id: int) -> Optional[Tesis]:
        return self.tesis.get(id)
    
    def actualizar(self, id: int, titulo: str, autor: str, escuela: str) -> Optional[Tesis]:
        if id in self.tesis:
            self.tesis[id].titulo = titulo
            self.tesis[id].autor = autor
            self.tesis[id].escuela = escuela
            return self.tesis[id]
        return None
    
    def eliminar(self, id: int) -> bool:
        if id in self.tesis:
            del self.tesis[id]
            return True
        return False


db = BaseDeDatos()


# ═══════════════════════════════════════════════════════════════
# ESQUEMAS DE VALIDACIÓN
# ═══════════════════════════════════════════════════════════════

class TesisInput(BaseModel):
    titulo: str
    autor: str
    escuela: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "titulo": "Mi tesis sobre inteligencia artificial",
                "autor": "Tu Nombre",
                "escuela": "Ingeniería de Sistemas"
            }
        }


# ═══════════════════════════════════════════════════════════════
# CONTROLADOR - ENDPOINTS
# ═══════════════════════════════════════════════════════════════

app = FastAPI(
    title="🎓 API de Tesis UNAP",
    description="API REST para gestión de tesis - Laboratorio MVC",
    version="1.0.0"
)

# ═══════════════════════════════════════════════════════════════
# CONFIGURACIÓN CORS
# ═══════════════════════════════════════════════════════════════

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ═══════════════════════════════════════════════════════════════
# ENDPOINTS
# ═══════════════════════════════════════════════════════════════

@app.get("/", tags=["Inicio"])
def inicio():
    """Página de inicio"""
    return {
        "mensaje": "🎓 Bienvenido a la API de Tesis UNAP",
        "documentacion": "Visita /docs para ver todos los endpoints"
    }


@app.get("/api/tesis", tags=["Tesis"])
def listar_tesis():
    """📋 Listar todas las tesis"""
    tesis = db.obtener_todos()
    return {"total": len(tesis), "items": tesis}


@app.get("/api/tesis/{id}", tags=["Tesis"])
def obtener_tesis(id: int):
    """🔍 Obtener una tesis por ID"""
    tesis = db.obtener_por_id(id)
    if not tesis:
        raise HTTPException(status_code=404, detail=f"Tesis {id} no encontrada")
    return {"data": tesis.to_dict()}


@app.post("/api/tesis", status_code=201, tags=["Tesis"])
def crear_tesis(datos: TesisInput):
    """➕ Crear nueva tesis"""
    if len(datos.titulo) < 10:
        raise HTTPException(status_code=400, detail="Título muy corto (mínimo 10 caracteres)")
    
    nueva = db.insertar(datos.titulo, datos.autor, datos.escuela)
    return {"mensaje": "✅ Tesis creada", "data": nueva.to_dict()}


@app.put("/api/tesis/{id}", tags=["Tesis"])
def actualizar_tesis(id: int, datos: TesisInput):
    """✏️ Actualizar tesis"""
    tesis = db.actualizar(id, datos.titulo, datos.autor, datos.escuela)
    if not tesis:
        raise HTTPException(status_code=404, detail=f"Tesis {id} no encontrada")
    return {"mensaje": "✅ Tesis actualizada", "data": tesis.to_dict()}


@app.delete("/api/tesis/{id}", tags=["Tesis"])
def eliminar_tesis(id: int):
    """🗑️ Eliminar tesis"""
    if not db.eliminar(id):
        raise HTTPException(status_code=404, detail=f"Tesis {id} no encontrada")
    return {"mensaje": f"✅ Tesis {id} eliminada"}


@app.get("/api/stats", tags=["Utilidades"])
def estadisticas():
    """📊 Estadísticas del sistema"""
    tesis = db.obtener_todos()
    return {"total_tesis": len(tesis)}


# ═══════════════════════════════════════════════════════════════
# EJECUTAR SERVIDOR
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*50)
    print("🚀 SERVIDOR INICIADO")
    print("="*50)
    print("📍 API: http://localhost:8000")
    print("📚 Docs: http://localhost:8000/docs")
    print("="*50 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)