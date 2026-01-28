"""
FUNCIONES DE SEGURIDAD
Hash de passwords y creacion de tokens JWT

Sesion 4: Autenticacion JWT
Curso: Desarrollo de Software - UNAP
"""

import os
from datetime import datetime, timedelta
import bcrypt
from jose import jwt

# Configuracion - Cambiar SECRET_KEY en produccion!
SECRET_KEY = os.getenv("SECRET_KEY", "clave-secreta-cambiar-en-produccion")
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30


def hash_password(password: str) -> str:
    """
    Convierte un password en texto plano a hash bcrypt.

    El hash es irreversible: no se puede obtener el password original.
    bcrypt es lento a proposito para dificultar ataques de fuerza bruta.

    Args:
        password: Password en texto plano

    Returns:
        Hash bcrypt del password
    """
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si un password coincide con su hash.

    Args:
        plain_password: Password en texto plano
        hashed_password: Hash almacenado en la BD

    Returns:
        True si coinciden, False si no
    """
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


def create_token(data: dict) -> str:
    """
    Crea un token JWT firmado con expiracion.

    El token contiene:
    - Los datos pasados (ej: user_id, email)
    - Fecha de expiracion (exp)
    - Firma criptografica

    Args:
        data: Diccionario con datos a incluir en el token

    Returns:
        Token JWT como string
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    """
    Decodifica y verifica un token JWT.

    Args:
        token: Token JWT a verificar

    Returns:
        Payload del token si es valido

    Raises:
        JWTError: Si el token es invalido o expiro
    """
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
