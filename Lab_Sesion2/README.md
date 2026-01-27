# 🚀 Laboratorio MVC - Sesión 2

## Instalación rápida

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar servidor
python main.py
```

## Probar la API

### Opción 1: Navegador
Abre http://localhost:8000/docs

### Opción 2: Script de pruebas
```bash
python test_api.py
```

### Opción 3: curl
```bash
# Listar
curl http://localhost:8000/api/tesis

# Crear
curl -X POST http://localhost:8000/api/tesis \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Mi tesis de prueba", "autor": "Mi Nombre", "escuela": "Sistemas"}'
```

## Estructura MVC

```
main.py
├── Tesis (MODEL)           → Define los datos
├── BaseDeDatos (MODEL)     → Simula PostgreSQL
├── TesisInput (SCHEMA)     → Valida entrada
└── Endpoints (CONTROLLER)  → Procesa peticiones
    ├── GET /api/tesis
    ├── GET /api/tesis/{id}
    ├── POST /api/tesis
    ├── PUT /api/tesis/{id}
    └── DELETE /api/tesis/{id}
```

## Docente
Milton Vladimir Mamani Calisaya
Universidad Nacional del Altiplano - Puno
