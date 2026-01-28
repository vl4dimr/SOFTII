"""
MODELO: USUARIO
Tabla de usuarios para autenticacion

Sesion 4: Autenticacion JWT
Curso: Desarrollo de Software - UNAP
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database import Base


class Usuario(Base):
    """
    Modelo SQLAlchemy para la tabla 'usuarios'

    Campos:
        id: Identificador unico
        email: Email del usuario (unico)
        password_hash: Hash bcrypt del password (NUNCA el password real)
        nombre: Nombre completo
        activo: Si el usuario puede hacer login
        created_at: Fecha de registro
    """
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(200), unique=True, nullable=False)
    password_hash = Column(String(200), nullable=False)
    nombre = Column(String(200))
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Usuario(id={self.id}, email='{self.email}')>"
