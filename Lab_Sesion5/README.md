# Laboratorio Sesion 5: Generacion de Documentos DOCX

API REST con generacion automatica de documentos Word en formato UNAP.

## Requisitos

- Python 3.8+
- PostgreSQL (base de datos `qillqay`)
- pip

## Inicio rapido

```bash
cd Lab_Sesion5
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Abrir http://localhost:8000/docs para la documentacion interactiva.

## Configuracion

Archivo `.env`:
```
DATABASE_URL=postgresql://postgres:admin@localhost:5432/qillqay
```

Las tablas se crean automaticamente al iniciar.

## Endpoints

### Tesis (CRUD)
| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| GET | `/api/tesis` | Listar tesis |
| GET | `/api/tesis/{id}` | Obtener por ID |
| GET | `/api/tesis/buscar/?q=texto` | Buscar por titulo |
| POST | `/api/tesis` | Crear tesis |
| PUT | `/api/tesis/{id}` | Actualizar tesis |
| PATCH | `/api/tesis/{id}/estado?estado=aprobado` | Cambiar estado |
| DELETE | `/api/tesis/{id}` | Eliminar tesis |

### Documentos (DOCX)
| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| GET | `/documentos/tesis/{id}/preview` | Vista previa de datos |
| GET | `/documentos/tesis/{id}/docx` | Descargar documento Word |

## Ejemplo de uso

```bash
# 1. Crear una tesis
curl -X POST http://localhost:8000/api/tesis \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Mi tesis sobre IA","autor":"Juan Perez","escuela":"Ing. Sistemas"}'

# 2. Descargar como DOCX
curl -O http://localhost:8000/documentos/tesis/1/docx
```

## Demos

Scripts ejecutables en la carpeta `demos/`:

```bash
python demos/demo1_basico.py       # Documento basico
python demos/demo2_formato.py      # Formato de texto (Runs)
python demos/demo3_margenes.py     # Margenes formato UNAP
python demos/demo4_tablas.py       # Tabla de jurados
python demos/demo5_portada_unap.py # Portada UNAP completa
python demos/demo6_api.py          # Flujo completo API (requiere servidor)
```

## Estructura

```
Lab_Sesion5/
  app/
    main.py                # FastAPI app
    database.py            # Conexion PostgreSQL
    models/tesis.py        # Modelo SQLAlchemy
    routes/tesis.py        # CRUD endpoints
    routes/documentos.py   # Endpoints DOCX
    schemas/tesis.py       # Validacion Pydantic
    services/
      docx_generator.py   # Generador de documentos
  demos/                   # Scripts de demostracion
  .env                     # Configuracion DB
  requirements.txt         # Dependencias
```

## Tecnologias

- **FastAPI** - Framework web
- **SQLAlchemy** - ORM para PostgreSQL
- **python-docx** - Generacion de documentos Word
- **Pydantic** - Validacion de datos
