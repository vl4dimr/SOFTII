# Ingeniería de Software II - UNAP

Laboratorios del curso **Ingeniería de Software II** de la Facultad de Ingeniería Estadística e Informática, Universidad Nacional del Altiplano - Puno.

**Proyecto:** Qillqay - Sistema de gestión de tesis con generación automática de documentos.

**Docente:** Milton Vladimir Mamani Calisaya

---

## Descripción del Proyecto

Qillqay es una API REST que evoluciona sesión a sesión: desde un CRUD básico en memoria hasta un sistema completo con base de datos, autenticación JWT, frontend React y generación automática de documentos Word en formato UNAP.

Cada laboratorio construye sobre los conceptos anteriores:

```
Sesión 2          Sesión 3              Sesión 4           Sesión 5
API básica   -->  + PostgreSQL     -->  + JWT Auth    -->  + Generación DOCX
MVC en memoria    + SQLAlchemy          + bcrypt           + python-docx
                  + React frontend      + Protección       + StreamingResponse
```

---

## Laboratorios

### Lab 2: API REST con FastAPI (MVC en memoria)

| | |
|---|---|
| **Tema** | Arquitectura MVC, endpoints REST, validación Pydantic |
| **Persistencia** | Lista en memoria (sin base de datos) |
| **Archivos** | 4 |
| **Líneas de código** | 362 |
| **Endpoints** | 7 |

```
GET    /api/tesis          Listar tesis
GET    /api/tesis/{id}     Obtener por ID
POST   /api/tesis          Crear tesis
PUT    /api/tesis/{id}     Actualizar tesis
DELETE /api/tesis/{id}     Eliminar tesis
GET    /api/stats          Estadísticas
GET    /                   Info de la API
```

**Iniciar:**
```bash
cd Lab_Sesion2
pip install -r requirements.txt
uvicorn main:app --reload
```

---

### Lab 3: Base de Datos + Frontend React

| | |
|---|---|
| **Tema** | SQLAlchemy ORM, PostgreSQL, paginación, búsqueda, frontend SPA |
| **Persistencia** | PostgreSQL (base de datos `qillqay`) |
| **Archivos** | 19 (12 backend + 7 frontend) |
| **Líneas de código** | 1,183 |
| **Endpoints** | 9 |
| **Frontend** | React 19 + Vite 6 |

```
GET    /api/tesis              Listar (con paginación skip/limit)
GET    /api/tesis/buscar/      Buscar por título, estado, escuela
GET    /api/tesis/{id}         Obtener por ID
POST   /api/tesis              Crear tesis
PUT    /api/tesis/{id}         Actualizar tesis
PATCH  /api/tesis/{id}/estado  Cambiar estado (borrador/revision/aprobado/rechazado)
DELETE /api/tesis/{id}         Eliminar tesis
GET    /                       Info de la API
GET    /api/health             Health check
```

**Frontend React:**
- CRUD completo visual con tema oscuro
- Tarjetas coloreadas por estado
- Búsqueda en tiempo real
- Modal de creación/edición
- Estadísticas en vivo
- Notificaciones toast

**Iniciar:**
```bash
# Terminal 1: Backend
cd Lab_Sesion3
pip install -r requirements.txt
uvicorn app.main:app --reload        # http://localhost:8000

# Terminal 2: Frontend
cd Lab_Sesion3/frontend
npm install
npx vite                             # http://localhost:5174
```

---

### Lab 4: Autenticación JWT

| | |
|---|---|
| **Tema** | JSON Web Tokens, bcrypt, protección de endpoints, HTTPBearer |
| **Persistencia** | PostgreSQL (tabla `usuarios`) |
| **Archivos** | 12 |
| **Líneas de código** | 464 |
| **Endpoints** | 5 |

```
POST   /auth/register    Registro de usuario (bcrypt hash)
POST   /auth/login       Login (retorna JWT Bearer token)
GET    /auth/me           Perfil del usuario (requiere token)
GET    /                  Info de la API
GET    /api/health        Health check
```

**Flujo de autenticación:**
```
Registro: password --> bcrypt.hash --> BD (password_hash)
Login:    password --> bcrypt.verify --> JWT token (30 min)
Acceso:   Authorization: Bearer <token> --> decode --> user_id
```

**Iniciar:**
```bash
cd Lab_Sesion4
pip install -r requirements.txt
uvicorn app.main:app --reload        # http://localhost:8000
```

---

### Lab 5: Generación de Documentos DOCX

| | |
|---|---|
| **Tema** | python-docx, formato UNAP, BytesIO, StreamingResponse |
| **Persistencia** | PostgreSQL (tabla `tesis`) |
| **Archivos** | 23 (17 backend + 6 demos) |
| **Líneas de código** | 935 |
| **Endpoints** | 11 |
| **Demos** | 6 scripts ejecutables |

```
GET    /documentos/tesis/{id}/docx      Descargar documento Word
GET    /documentos/tesis/{id}/preview   Vista previa de datos
GET    /api/tesis                       Listar tesis
POST   /api/tesis                       Crear tesis
PUT    /api/tesis/{id}                  Actualizar tesis
PATCH  /api/tesis/{id}/estado           Cambiar estado
DELETE /api/tesis/{id}                  Eliminar tesis
...
```

**Documento generado incluye:**
- Portada UNAP completa (universidad, facultad, escuela, título, autor)
- Márgenes formato tesis: izquierdo 4cm (empaste), resto 2.5cm
- Fuente Times New Roman 12pt, interlineado 1.5
- Tabla de jurados calificadores
- Descarga directa desde la API (sin archivos temporales en disco)

**Demos disponibles:**
```bash
python demos/demo1_basico.py        # Documento básico
python demos/demo2_formato.py       # Formato de texto (Runs)
python demos/demo3_margenes.py      # Márgenes formato UNAP
python demos/demo4_tablas.py        # Tabla de jurados
python demos/demo5_portada_unap.py  # Portada UNAP completa
python demos/demo6_api.py           # Flujo completo API (requiere servidor)
```

**Iniciar:**
```bash
cd Lab_Sesion5
pip install -r requirements.txt
uvicorn app.main:app --reload        # http://localhost:8000
```

---

## Métricas del Proyecto

| Métrica | Valor |
|---------|-------|
| Laboratorios | 4 |
| Archivos de código | 58 |
| Líneas de código totales | 2,944 |
| Endpoints REST | 32 |
| Modelos de BD | 2 (Tesis, Usuario) |
| Demos ejecutables | 6 |
| Frontend React | 1 SPA completa |
| Dependencias Python | 11 librerías |
| Dependencias Node | 2 (react, react-dom) |

### Líneas de código por laboratorio

```
Lab 2  ████████░░░░░░░░░░░░░░░░░░░░░░  362 líneas   (12%)
Lab 3  ████████████████████████░░░░░░  1,183 líneas  (40%)
Lab 4  █████████░░░░░░░░░░░░░░░░░░░░░  464 líneas   (16%)
Lab 5  ███████████████████░░░░░░░░░░░  935 líneas   (32%)
       ──────────────────────────────
       Total: 2,944 líneas
```

### Endpoints por laboratorio

```
Lab 2  ██████████████░░░░░░░░░░░░░░░░  7 endpoints
Lab 3  ██████████████████░░░░░░░░░░░░  9 endpoints
Lab 4  ██████████░░░░░░░░░░░░░░░░░░░░  5 endpoints
Lab 5  ██████████████████████░░░░░░░░  11 endpoints
       ──────────────────────────────
       Total: 32 endpoints
```

---

## Stack Tecnológico

### Backend
| Tecnología | Version | Uso |
|-----------|---------|-----|
| Python | 3.8+ | Lenguaje principal |
| FastAPI | 0.109+ | Framework REST API |
| SQLAlchemy | 2.0+ | ORM para PostgreSQL |
| Pydantic | 2.5+ | Validación de datos |
| PostgreSQL | 15+ | Base de datos relacional |
| bcrypt | 4.0+ | Hash de passwords |
| python-jose | 3.3+ | Tokens JWT |
| python-docx | 1.1+ | Generación Word |
| Uvicorn | 0.27+ | Servidor ASGI |

### Frontend
| Tecnología | Version | Uso |
|-----------|---------|-----|
| React | 19.x | Librería UI |
| Vite | 6.x | Bundler y dev server |
| CSS puro | - | Estilos dark theme |

---

## Requisitos

- **Python** 3.8 o superior
- **Node.js** 18 o superior (solo Lab 3 frontend)
- **PostgreSQL** con base de datos `qillqay` creada (Labs 3, 4, 5)

### Configuración de base de datos

```sql
CREATE DATABASE qillqay;
```

Archivo `.env` en cada lab (Labs 3, 4, 5):
```
DATABASE_URL=postgresql://postgres:admin@localhost:5432/qillqay
```

---

## Estructura del Repositorio

```
SOFTII/
├── Lab_Sesion2/              # API REST MVC en memoria
│   ├── main.py               #   App FastAPI (todo en un archivo)
│   ├── test_api.py            #   Tests con requests
│   └── requirements.txt
│
├── Lab_Sesion3/              # CRUD + PostgreSQL + React
│   ├── app/
│   │   ├── main.py            #   FastAPI + CORS
│   │   ├── database.py        #   Conexión SQLAlchemy
│   │   ├── models/tesis.py    #   Modelo ORM Tesis
│   │   ├── routes/tesis.py    #   Endpoints CRUD
│   │   └── schemas/tesis.py   #   Validación Pydantic
│   ├── frontend/              #   React SPA
│   │   ├── src/App.jsx        #     Componente CRUD completo
│   │   ├── src/api.js         #     Funciones fetch API
│   │   ├── src/index.css      #     Estilos dark theme
│   │   └── vite.config.js     #     Config Vite (port 5174)
│   └── requirements.txt
│
├── Lab_Sesion4/              # Autenticación JWT
│   ├── app/
│   │   ├── main.py            #   FastAPI app
│   │   ├── database.py        #   Conexión PostgreSQL
│   │   ├── auth/
│   │   │   ├── security.py    #   bcrypt + JWT funciones
│   │   │   └── dependencies.py#   Dependencias FastAPI
│   │   ├── models/usuario.py  #   Modelo ORM Usuario
│   │   └── routes/auth.py     #   Register, Login, Me
│   └── requirements.txt
│
├── Lab_Sesion5/              # Generación DOCX
│   ├── app/
│   │   ├── main.py            #   FastAPI app
│   │   ├── database.py        #   Conexión PostgreSQL
│   │   ├── models/tesis.py    #   Modelo ORM Tesis
│   │   ├── routes/
│   │   │   ├── tesis.py       #   CRUD tesis
│   │   │   └── documentos.py  #   Descarga DOCX
│   │   ├── schemas/tesis.py   #   Validacion
│   │   └── services/
│   │       └── docx_generator.py  # Generador documentos
│   ├── demos/                 #   6 scripts de demostración
│   └── requirements.txt
│
├── .gitignore
└── README.md                  # Este archivo
```

---

## Autor

**Milton Vladimir Mamani Calisaya**
Universidad Nacional del Altiplano - Puno
Facultad de Ingeniería Estadística e Informática
