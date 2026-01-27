"""
RUTAS DE DOCUMENTOS
Endpoints para generar y descargar documentos

Sesion 5: Generacion de Documentos
Curso: Desarrollo de Software - UNAP
"""

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from io import BytesIO

from app.database import get_db
from app.models.tesis import Tesis
from app.services.docx_generator import generar_tesis, generar_desde_plantilla

router = APIRouter(prefix="/documentos", tags=["Documentos"])


@router.get("/tesis/{tesis_id}/docx")
def descargar_tesis_docx(tesis_id: int, db: Session = Depends(get_db)):
    """
    DESCARGAR TESIS EN FORMATO DOCX
    
    GET /documentos/tesis/{id}/docx
    
    Genera un documento Word con formato UNAP y lo retorna como descarga.
    """
    # Obtener tesis de la base de datos
    tesis = db.query(Tesis).filter(Tesis.id == tesis_id).first()
    
    if not tesis:
        raise HTTPException(
            status_code=404,
            detail=f"Tesis con ID {tesis_id} no encontrada"
        )
    
    # Preparar datos para el generador
    datos = {
        "titulo": tesis.titulo,
        "autor": tesis.autor,
        "escuela": tesis.escuela if hasattr(tesis, 'escuela') else "ESCUELA PROFESIONAL",
        "anio": "2026"
    }
    
    # Generar documento
    doc = generar_tesis(datos)
    
    # Guardar en memoria (BytesIO en vez de archivo)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)  # Volver al inicio del buffer
    
    # Nombre del archivo para descarga
    nombre_archivo = f"tesis_{tesis_id}_{tesis.autor.replace(' ', '_')}.docx"
    
    # Retornar como descarga
    return StreamingResponse(
        buffer,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={
            "Content-Disposition": f"attachment; filename={nombre_archivo}"
        }
    )


@router.get("/tesis/{tesis_id}/preview")
def preview_tesis(tesis_id: int, db: Session = Depends(get_db)):
    """
    PREVIEW DE DATOS DE TESIS
    
    GET /documentos/tesis/{id}/preview
    
    Retorna los datos que se usarian para generar el documento.
    Util para verificar antes de generar.
    """
    tesis = db.query(Tesis).filter(Tesis.id == tesis_id).first()
    
    if not tesis:
        raise HTTPException(
            status_code=404,
            detail=f"Tesis con ID {tesis_id} no encontrada"
        )
    
    return {
        "id": tesis.id,
        "titulo": tesis.titulo,
        "autor": tesis.autor,
        "escuela": getattr(tesis, 'escuela', "No especificada"),
        "estado": tesis.estado,
        "formato_disponible": ["docx"],
        "endpoint_descarga": f"/documentos/tesis/{tesis_id}/docx"
    }
