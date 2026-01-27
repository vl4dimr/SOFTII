"""
SCRIPT DE PRUEBAS - API de Tesis
Ejecutar: python test_api.py

Asegúrate de que el servidor esté corriendo primero:
python main.py
"""

import requests

BASE_URL = "http://localhost:8000/api"

def separador(titulo):
    print(f"\n{'='*50}")
    print(f"  {titulo}")
    print('='*50)

def probar_api():
    separador("🧪 INICIANDO PRUEBAS DE LA API")
    
    # ─────────────────────────────────────────────────
    # 1. LISTAR TESIS
    # ─────────────────────────────────────────────────
    separador("📋 1. GET /api/tesis - Listar todas")
    
    response = requests.get(f"{BASE_URL}/tesis")
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Total de tesis: {data['total']}")
    
    for tesis in data['items']:
        print(f"  - [{tesis['id']}] {tesis['titulo'][:40]}...")
    
    # ─────────────────────────────────────────────────
    # 2. OBTENER UNA TESIS
    # ─────────────────────────────────────────────────
    separador("🔍 2. GET /api/tesis/1 - Obtener por ID")
    
    response = requests.get(f"{BASE_URL}/tesis/1")
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        tesis = response.json()['data']
        print(f"Título: {tesis['titulo']}")
        print(f"Autor: {tesis['autor']}")
        print(f"Estado: {tesis['estado']}")
    
    # ─────────────────────────────────────────────────
    # 3. CREAR NUEVA TESIS
    # ─────────────────────────────────────────────────
    separador("➕ 3. POST /api/tesis - Crear nueva")
    
    nueva_tesis = {
        "titulo": "Sistema de reconocimiento facial con Python y OpenCV",
        "autor": "Estudiante UNAP",
        "escuela": "Ing. Sistemas"
    }
    
    print(f"Enviando: {nueva_tesis}")
    response = requests.post(f"{BASE_URL}/tesis", json=nueva_tesis)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 201:
        data = response.json()
        nuevo_id = data['data']['id']
        print(f"✅ Tesis creada con ID: {nuevo_id}")
    else:
        print(f"❌ Error: {response.json()}")
        nuevo_id = None
    
    # ─────────────────────────────────────────────────
    # 4. ACTUALIZAR TESIS
    # ─────────────────────────────────────────────────
    if nuevo_id:
        separador(f"✏️ 4. PUT /api/tesis/{nuevo_id} - Actualizar")
        
        datos_actualizados = {
            "titulo": "Sistema de reconocimiento facial para control de asistencia",
            "autor": "Estudiante UNAP - Actualizado",
            "escuela": "Ing. Sistemas"
        }
        
        response = requests.put(f"{BASE_URL}/tesis/{nuevo_id}", json=datos_actualizados)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            print(f"✅ Nuevo título: {response.json()['data']['titulo']}")
    
    # ─────────────────────────────────────────────────
    # 5. PROBAR ERROR 404
    # ─────────────────────────────────────────────────
    separador("❓ 5. GET /api/tesis/999 - Probar 404")
    
    response = requests.get(f"{BASE_URL}/tesis/999")
    print(f"Status: {response.status_code}")
    print(f"Mensaje: {response.json()['detail']}")
    
    # ─────────────────────────────────────────────────
    # 6. PROBAR ERROR 400
    # ─────────────────────────────────────────────────
    separador("⚠️ 6. POST con título corto - Probar 400")
    
    tesis_invalida = {
        "titulo": "Corto",  # Menos de 10 caracteres
        "autor": "Test",
        "escuela": "Test"
    }
    
    response = requests.post(f"{BASE_URL}/tesis", json=tesis_invalida)
    print(f"Status: {response.status_code}")
    print(f"Mensaje: {response.json()['detail']}")
    
    # ─────────────────────────────────────────────────
    # 7. ELIMINAR TESIS
    # ─────────────────────────────────────────────────
    if nuevo_id:
        separador(f"🗑️ 7. DELETE /api/tesis/{nuevo_id} - Eliminar")
        
        response = requests.delete(f"{BASE_URL}/tesis/{nuevo_id}")
        print(f"Status: {response.status_code}")
        print(f"Mensaje: {response.json()['mensaje']}")
        
        # Verificar eliminación
        print("\nVerificando eliminación...")
        response = requests.get(f"{BASE_URL}/tesis/{nuevo_id}")
        print(f"Status al buscar: {response.status_code} (404 = Eliminado ✅)")
    
    # ─────────────────────────────────────────────────
    # 8. ESTADÍSTICAS
    # ─────────────────────────────────────────────────
    separador("📊 8. GET /api/stats - Estadísticas")
    
    response = requests.get(f"{BASE_URL}/stats")
    print(f"Status: {response.status_code}")
    print(f"Total tesis: {response.json()['total_tesis']}")
    
    # ─────────────────────────────────────────────────
    # RESUMEN
    # ─────────────────────────────────────────────────
    separador("✅ PRUEBAS COMPLETADAS")
    print("""
    Resumen de códigos HTTP probados:
    - 200 OK: Operación exitosa
    - 201 Created: Recurso creado
    - 400 Bad Request: Datos inválidos
    - 404 Not Found: Recurso no existe
    """)


if __name__ == "__main__":
    try:
        probar_api()
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: No se puede conectar al servidor")
        print("   Asegúrate de ejecutar primero: python main.py")
