"""
RUTAS DE AUTENTICACION
Endpoints para registro y login

Sesion 4: Autenticacion JWT
Curso: Desarrollo de Software - UNAP
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models.usuario import Usuario
from app.auth.security import hash_password, verify_password, create_token
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Autenticacion"])


# Schemas para validacion
class RegistroInput(BaseModel):
    email: str
    password: str
    nombre: str


class LoginInput(BaseModel):
    email: str
    password: str


class TokenOutput(BaseModel):
    token: str
    tipo: str = "bearer"


# Endpoints

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(datos: RegistroInput, db: Session = Depends(get_db)):
    """
    REGISTRO DE USUARIO

    POST /auth/register
    Body: {"email": "...", "password": "...", "nombre": "..."}

    El password se guarda como hash bcrypt, NUNCA en texto plano.
    """
    # Verificar si el email ya existe
    existe = db.query(Usuario).filter(Usuario.email == datos.email).first()
    if existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email ya esta registrado"
        )

    # Crear usuario con password hasheado
    nuevo_usuario = Usuario(
        email=datos.email,
        password_hash=hash_password(datos.password),
        nombre=datos.nombre
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {
        "mensaje": "Usuario creado exitosamente",
        "id": nuevo_usuario.id,
        "email": nuevo_usuario.email
    }


@router.post("/login", response_model=TokenOutput)
def login(datos: LoginInput, db: Session = Depends(get_db)):
    """
    LOGIN DE USUARIO

    POST /auth/login
    Body: {"email": "...", "password": "..."}

    Retorna un token JWT que debe enviarse en el header Authorization.
    """
    # Buscar usuario por email
    usuario = db.query(Usuario).filter(Usuario.email == datos.email).first()

    # Verificar credenciales
    if not usuario or not verify_password(datos.password, usuario.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales invalidas"
        )

    # Verificar que este activo
    if not usuario.activo:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario inactivo"
        )

    # Crear token JWT
    token = create_token({
        "user_id": usuario.id,
        "email": usuario.email
    })

    return {"token": token, "tipo": "bearer"}


@router.get("/me")
def perfil(user: dict = Depends(get_current_user)):
    """
    OBTENER PERFIL DEL USUARIO ACTUAL

    GET /auth/me
    Header: Authorization: Bearer <token>

    Endpoint protegido que retorna los datos del usuario logueado.
    """
    return {
        "user_id": user.get("user_id"),
        "email": user.get("email")
    }
