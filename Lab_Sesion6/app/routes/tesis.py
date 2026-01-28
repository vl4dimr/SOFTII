"""
CONTROLADOR: ENDPOINTS DE TESIS
CRUD completo con SQLAlchemy y PostgreSQL
Protegido con JWT (Sesion 6)

Curso: Desarrollo de Software - UNAP
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.tesis import Tesis
from app.schemas.tesis import TesisInput, TesisOutput
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/api/tesis", tags=["Tesis"])


@router.get("", response_model=List[TesisOutput])
def listar(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    LISTAR TESIS

    GET /api/tesis
    GET /api/tesis?skip=0&limit=10
    Header: Authorization: Bearer <token>

    Equivalente SQL: SELECT * FROM tesis LIMIT ? OFFSET ?
    """
    tesis = db.query(Tesis).offset(skip).limit(limit).all()
    return tesis


@router.get("/buscar/", response_model=List[TesisOutput])
def buscar(
    q: str = None,
    estado: str = None,
    escuela: str = None,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    BUSCAR TESIS

    GET /api/tesis/buscar/?q=machine&estado=aprobado
    Header: Authorization: Bearer <token>

    Parametros opcionales:
    - q: Buscar en titulo
    - estado: Filtrar por estado
    - escuela: Filtrar por escuela
    """
    query = db.query(Tesis)

    if q:
        query = query.filter(Tesis.titulo.ilike(f"%{q}%"))

    if estado:
        query = query.filter(Tesis.estado == estado)

    if escuela:
        query = query.filter(Tesis.escuela.ilike(f"%{escuela}%"))

    return query.all()


@router.get("/{id}", response_model=TesisOutput)
def obtener(
    id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    OBTENER TESIS POR ID

    GET /api/tesis/{id}
    Header: Authorization: Bearer <token>

    Equivalente SQL: SELECT * FROM tesis WHERE id = ?
    """
    tesis = db.query(Tesis).filter(Tesis.id == id).first()

    if not tesis:
        raise HTTPException(
            status_code=404,
            detail=f"Tesis con ID {id} no encontrada"
        )

    return tesis


@router.post("", response_model=TesisOutput, status_code=201)
def crear(
    datos: TesisInput,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    CREAR TESIS

    POST /api/tesis
    Header: Authorization: Bearer <token>
    Body: {"titulo": "...", "autor": "...", "escuela": "..."}

    Equivalente SQL: INSERT INTO tesis (titulo, autor, escuela) VALUES (?, ?, ?)
    """
    # Crear instancia del modelo
    nueva_tesis = Tesis(
        titulo=datos.titulo,
        autor=datos.autor,
        escuela=datos.escuela
    )

    # Agregar a la sesion
    db.add(nueva_tesis)

    # Guardar en BD
    db.commit()

    # Refrescar para obtener el ID generado
    db.refresh(nueva_tesis)

    return nueva_tesis


@router.put("/{id}", response_model=TesisOutput)
def actualizar(
    id: int,
    datos: TesisInput,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    ACTUALIZAR TESIS

    PUT /api/tesis/{id}
    Header: Authorization: Bearer <token>
    Body: {"titulo": "...", "autor": "...", "escuela": "..."}

    Equivalente SQL: UPDATE tesis SET titulo=?, autor=?, escuela=? WHERE id=?
    """
    tesis = db.query(Tesis).filter(Tesis.id == id).first()

    if not tesis:
        raise HTTPException(
            status_code=404,
            detail=f"Tesis con ID {id} no encontrada"
        )

    # Actualizar campos
    tesis.titulo = datos.titulo
    tesis.autor = datos.autor
    tesis.escuela = datos.escuela

    # Guardar cambios
    db.commit()
    db.refresh(tesis)

    return tesis


@router.patch("/{id}/estado")
def cambiar_estado(
    id: int,
    estado: str,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    CAMBIAR ESTADO

    PATCH /api/tesis/{id}/estado?estado=aprobado
    Header: Authorization: Bearer <token>

    Estados validos: borrador, revision, aprobado, rechazado
    """
    estados_validos = ["borrador", "revision", "aprobado", "rechazado"]

    if estado not in estados_validos:
        raise HTTPException(
            status_code=400,
            detail=f"Estado invalido. Validos: {estados_validos}"
        )

    tesis = db.query(Tesis).filter(Tesis.id == id).first()

    if not tesis:
        raise HTTPException(
            status_code=404,
            detail=f"Tesis con ID {id} no encontrada"
        )

    tesis.estado = estado
    db.commit()

    return {"mensaje": f"Estado actualizado a '{estado}'", "id": id}


@router.delete("/{id}")
def eliminar(
    id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    ELIMINAR TESIS

    DELETE /api/tesis/{id}
    Header: Authorization: Bearer <token>

    Equivalente SQL: DELETE FROM tesis WHERE id = ?
    """
    tesis = db.query(Tesis).filter(Tesis.id == id).first()

    if not tesis:
        raise HTTPException(
            status_code=404,
            detail=f"Tesis con ID {id} no encontrada"
        )

    db.delete(tesis)
    db.commit()

    return {"mensaje": f"Tesis con ID {id} eliminada exitosamente"}
