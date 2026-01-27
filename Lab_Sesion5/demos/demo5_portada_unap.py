"""
DEMO 5: Portada completa formato UNAP
Ejecutar: python demos/demo5_portada_unap.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.docx_generator import generar_tesis

datos = {
    "titulo": "Sistema de Reconocimiento Facial para Control de Asistencia en la Universidad Nacional del Altiplano",
    "autor": "Juan Carlos Perez Lopez",
    "escuela": "ESCUELA PROFESIONAL DE INGENIERIA DE SISTEMAS",
    "titulo_profesional": "INGENIERO DE SISTEMAS",
    "anio": "2026",
    "jurados": [
        ("PRESIDENTE", "Carlos Mamani Diaz", "Dr."),
        ("PRIMER MIEMBRO", "Maria Garcia Quispe", "Mg."),
        ("SEGUNDO MIEMBRO", "Roberto Flores Condori", "Mg."),
    ]
}

doc = generar_tesis(datos)
doc.save("demos/demo5_resultado.docx")
print("Documento creado: demos/demo5_resultado.docx")
print()
print("Contenido generado:")
print("  - Portada UNAP completa")
print("  - Tabla de jurados calificadores")
print("  - Margenes: Izq 4cm, Der/Sup/Inf 2.5cm")
print("  - Fuente: Times New Roman")
