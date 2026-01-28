"""
DEPENDENCIES DE AUTENTICACION
Funciones para proteger endpoints

Sesion 4: Autenticacion JWT
Curso: Desarrollo de Software - UNAP
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.auth.security import SECRET_KEY, ALGORITHM
from app.database import get_db
from app.models.usuario import Usuario

# Esquema de seguridad HTTP Bearer
security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    """
    Extrae y valida el usuario del token JWT.

    Esta funcion se usa como Dependency en endpoints protegidos.

    Uso:
        @router.post("/")
        def crear(user: dict = Depends(get_current_user)):
            # user contiene {"user_id": 1, "email": "..."}
            ...

    Args:
        credentials: Token Bearer extraido del header Authorization

    Returns:
        Payload del token (dict con user_id, email, etc.)

    Raises:
        HTTPException 401: Si el token es invalido o expiro
    """
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalido o expirado",
            headers={"WWW-Authenticate": "Bearer"}
        )


def get_current_active_user(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> Usuario:
    """
    Obtiene el usuario completo de la BD y verifica que este activo.

    Uso cuando necesitas el objeto Usuario completo:
        @router.get("/me")
        def perfil(user: Usuario = Depends(get_current_active_user)):
            return {"email": user.email, "nombre": user.nombre}

    Args:
        current_user: Payload del token
        db: Sesion de base de datos

    Returns:
        Objeto Usuario de SQLAlchemy

    Raises:
        HTTPException 401: Si el usuario no existe o esta inactivo
    """
    usuario = db.query(Usuario).filter(
        Usuario.id == current_user.get("user_id")
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado"
        )

    if not usuario.activo:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario inactivo"
        )

    return usuario
