"""
MODELO: TESIS
Define la estructura de la tabla 'tesis' en PostgreSQL

Sesion 3: Bases de Datos
Curso: Desarrollo de Software - UNAP
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Tesis(Base):
    """
    Modelo SQLAlchemy para la tabla 'tesis'
    
    Equivalencias:
        Column(Integer)     → INTEGER
        Column(String(n))   → VARCHAR(n)
        Column(DateTime)    → TIMESTAMP
        primary_key=True    → PRIMARY KEY
        nullable=False      → NOT NULL
        default="x"         → DEFAULT 'x'
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
    
    # Ejemplo de relación (comentado por ahora)
    # autor_id = Column(Integer, ForeignKey("usuarios.id"))
    # autor = relationship("Usuario", back_populates="tesis")
    
    def __repr__(self):
        return f"<Tesis(id={self.id}, titulo='{self.titulo[:30]}...')>"


class Usuario(Base):
    """
    Modelo para la tabla 'usuarios' (para relaciones)
    """
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relación con tesis (comentado por ahora)
    # tesis = relationship("Tesis", back_populates="autor")
    
    def __repr__(self):
        return f"<Usuario(id={self.id}, email='{self.email}')>"
