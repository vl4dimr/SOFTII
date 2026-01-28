"""
MODELO: TESIS
Define la estructura de la tabla 'tesis' en PostgreSQL

Sesion 6: Aplicacion Completa
Curso: Desarrollo de Software - UNAP

NOTA: La clase Usuario esta en models/usuario.py (Lab 4).
      Aqui solo queda el modelo Tesis.
"""

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base


class Tesis(Base):
    """
    Modelo SQLAlchemy para la tabla 'tesis'

    Equivalencias:
        Column(Integer)     -> INTEGER
        Column(String(n))   -> VARCHAR(n)
        Column(DateTime)    -> TIMESTAMP
        primary_key=True    -> PRIMARY KEY
        nullable=False      -> NOT NULL
        default="x"         -> DEFAULT 'x'
    """
    __tablename__ = "tesis"

    # Columnas
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(500), nullable=False)
    autor = Column(String(200), nullable=False)
    escuela = Column(String(100))
    estado = Column(String(50), default="borrador")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Tesis(id={self.id}, titulo='{self.titulo[:30]}...')>"
