"""
DEMO 6: Flujo completo con la API
Ejecutar:
  1. Primero iniciar el servidor: uvicorn app.main:app --reload
  2. Luego: python demos/demo6_api.py
"""
import requests

BASE = "http://localhost:8000"

print("=" * 50)
print("DEMO 6: Flujo completo API + DOCX")
print("=" * 50)

# Paso 1: Crear una tesis
print("\n[1] Creando tesis...")
resp = requests.post(f"{BASE}/api/tesis", json={
    "titulo": "Implementacion de Machine Learning para Prediccion de Rendimiento Academico",
    "autor": "Ana Maria Quispe Condori",
    "escuela": "Ing. Sistemas"
})
tesis = resp.json()
tesis_id = tesis["id"]
print(f"    Tesis creada con ID: {tesis_id}")
print(f"    Titulo: {tesis['titulo']}")
print(f"    Autor: {tesis['autor']}")

# Paso 2: Preview
print(f"\n[2] Preview del documento...")
resp = requests.get(f"{BASE}/documentos/tesis/{tesis_id}/preview")
preview = resp.json()
print(f"    Estado: {preview['estado']}")
print(f"    Formatos: {preview['formato_disponible']}")
print(f"    Endpoint: {preview['endpoint_descarga']}")

# Paso 3: Descargar DOCX
print(f"\n[3] Descargando DOCX...")
resp = requests.get(f"{BASE}/documentos/tesis/{tesis_id}/docx")
filename = f"demos/demo6_tesis_{tesis_id}.docx"
with open(filename, "wb") as f:
    f.write(resp.content)
print(f"    Archivo: {filename}")
print(f"    Tamano: {len(resp.content):,} bytes")
print(f"    Status: {resp.status_code}")

print("\n" + "=" * 50)
print("Abre el archivo .docx para ver la tesis generada!")
print("=" * 50)
