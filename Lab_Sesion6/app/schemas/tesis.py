"""
ESQUEMAS DE VALIDACION
Pydantic para validar entrada y salida

Sesion 3: Bases de Datos
Curso: Desarrollo de Software - UNAP
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class TesisInput(BaseModel):
    """Esquema para crear/actualizar tesis"""
    titulo: str = Field(
        ...,
        min_length=10,
        max_length=500,
        description="Titulo de la tesis"
    )
    autor: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="Nombre del autor"
    )
    escuela: str = Field(
        default="Ingenieria de Sistemas",
        max_length=100,
        description="Escuela profesional"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "titulo": "Sistema de reconocimiento facial con Python y OpenCV",
                "autor": "Juan Carlos Perez Lopez",
                "escuela": "Ingenieria de Sistemas"
            }
        }


class TesisOutput(BaseModel):
    """Esquema de respuesta (incluye campos generados)"""
    id: int
    titulo: str
    autor: str
    escuela: Optional[str] = None
    estado: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # Permite convertir desde ORM
