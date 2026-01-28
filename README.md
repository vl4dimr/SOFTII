# Ingenieria de Software II - UNAP

Laboratorios del curso **Ingenieria de Software II** de la Facultad de Ingenieria Estadistica e Informatica, Universidad Nacional del Altiplano - Puno.

**Proyecto:** Qillqay - Sistema de gestion de tesis con generacion automatica de documentos.

**Docente:** Milton Vladimir Mamani Calisaya

---

## Descripcion del Proyecto

Qillqay es una API REST que evoluciona sesion a sesion: desde un CRUD basico en memoria hasta un sistema completo con base de datos, autenticacion JWT, frontend React y generacion automatica de documentos Word en formato UNAP.

Cada laboratorio construye sobre los conceptos anteriores:

```
Sesion 2          Sesion 3              Sesion 4           Sesion 5
API basica   -->  + PostgreSQL     -->  + JWT Auth    -->  + Generacion DOCX
MVC en memoria    + SQLAlchemy          + bcrypt           + python-docx
                  + React frontend      + Proteccion       + StreamingResponse
```

---

## Laboratorios

### Lab 2: API REST con FastAPI (MVC en memoria)

| | |
|---|---|
| **Tema** | Arquitectura MVC, endpoints REST, validacion Pydantic |
| **Persistencia** | Lista en memoria (sin base de datos) |
| **Archivos** | 4 |
| **Lineas de codigo** | 362 |
| **Endpoints** | 7 |

```
GET    /api/tesis          Listar tesis
GET    /api/tesis/{id}     Obtener por ID
POST   /api/tesis          Crear tesis
PUT    /api/tesis/{id}     Actualizar tesis
DELETE /api/tesis/{id}     Eliminar tesis
GET    /api/stats          Estadisticas
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
| **Tema** | SQLAlchemy ORM, PostgreSQL, paginacion, busqueda, frontend SPA |
| **Persistencia** | PostgreSQL (base de datos `qillqay`) |
| **Archivos** | 19 (12 backend + 7 frontend) |
| **Lineas de codigo** | 1,183 |
| **Endpoints** | 9 |
| **Frontend** | React 19 + Vite 6 |

```
GET    /api/tesis              Listar (con paginacion skip/limit)
GET    /api/tesis/buscar/      Buscar por titulo, estado, escuela
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
- Busqueda en tiempo real
- Modal de creacion/edicion
- Estadisticas en vivo
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

### Lab 4: Autenticacion JWT

| | |
|---|---|
| **Tema** | JSON Web Tokens, bcrypt, proteccion de endpoints, HTTPBearer |
| **Persistencia** | PostgreSQL (tabla `usuarios`) |
| **Archivos** | 12 |
| **Lineas de codigo** | 464 |
| **Endpoints** | 5 |

```
POST   /auth/register    Registro de usuario (bcrypt hash)
POST   /auth/login       Login (retorna JWT Bearer token)
GET    /auth/me           Perfil del usuario (requiere token)
GET    /                  Info de la API
GET    /api/health        Health check
```

**Flujo de autenticacion:**
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

### Lab 5: Generacion de Documentos DOCX

| | |
|---|---|
| **Tema** | python-docx, formato UNAP, BytesIO, StreamingResponse |
| **Persistencia** | PostgreSQL (tabla `tesis`) |
| **Archivos** | 23 (17 backend + 6 demos) |
| **Lineas de codigo** | 935 |
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
- Portada UNAP completa (universidad, facultad, escuela, titulo, autor)
- Margenes formato tesis: izquierdo 4cm (empaste), resto 2.5cm
- Fuente Times New Roman 12pt, interlineado 1.5
- Tabla de jurados calificadores
- Descarga directa desde la API (sin archivos temporales en disco)

**Demos disponibles:**
```bash
python demos/demo1_basico.py        # Documento basico
python demos/demo2_formato.py       # Formato de texto (Runs)
python demos/demo3_margenes.py      # Margenes formato UNAP
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

## Metricas del Proyecto

| Metrica | Valor |
|---------|-------|
| Laboratorios | 4 |
| Archivos de codigo | 58 |
| Lineas de codigo totales | 2,944 |
| Endpoints REST | 32 |
| Modelos de BD | 2 (Tesis, Usuario) |
| Demos ejecutables | 6 |
| Frontend React | 1 SPA completa |
| Dependencias Python | 11 librerias |
| Dependencias Node | 2 (react, react-dom) |

### Lineas de codigo por laboratorio

```
Lab 2  ████████░░░░░░░░░░░░░░░░░░░░░░  362 lineas   (12%)
Lab 3  ████████████████████████░░░░░░  1,183 lineas  (40%)
Lab 4  █████████░░░░░░░░░░░░░░░░░░░░░  464 lineas   (16%)
Lab 5  ███████████████████░░░░░░░░░░░  935 lineas   (32%)
       ──────────────────────────────
       Total: 2,944 lineas
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

## Stack Tecnologico

### Backend
| Tecnologia | Version | Uso |
|-----------|---------|-----|
| Python | 3.8+ | Lenguaje principal |
| FastAPI | 0.109+ | Framework REST API |
| SQLAlchemy | 2.0+ | ORM para PostgreSQL |
| Pydantic | 2.5+ | Validacion de datos |
| PostgreSQL | 15+ | Base de datos relacional |
| bcrypt | 4.0+ | Hash de passwords |
| python-jose | 3.3+ | Tokens JWT |
| python-docx | 1.1+ | Generacion Word |
| Uvicorn | 0.27+ | Servidor ASGI |

### Frontend
| Tecnologia | Version | Uso |
|-----------|---------|-----|
| React | 19.x | Libreria UI |
| Vite | 6.x | Bundler y dev server |
| CSS puro | - | Estilos dark theme |

---

## Requisitos

- **Python** 3.8 o superior
- **Node.js** 18 o superior (solo Lab 3 frontend)
- **PostgreSQL** con base de datos `qillqay` creada (Labs 3, 4, 5)

### Configuracion de base de datos

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
│   │   ├── database.py        #   Conexion SQLAlchemy
│   │   ├── models/tesis.py    #   Modelo ORM Tesis
│   │   ├── routes/tesis.py    #   Endpoints CRUD
│   │   └── schemas/tesis.py   #   Validacion Pydantic
│   ├── frontend/              #   React SPA
│   │   ├── src/App.jsx        #     Componente CRUD completo
│   │   ├── src/api.js         #     Funciones fetch API
│   │   ├── src/index.css      #     Estilos dark theme
│   │   └── vite.config.js     #     Config Vite (port 5174)
│   └── requirements.txt
│
├── Lab_Sesion4/              # Autenticacion JWT
│   ├── app/
│   │   ├── main.py            #   FastAPI app
│   │   ├── database.py        #   Conexion PostgreSQL
│   │   ├── auth/
│   │   │   ├── security.py    #   bcrypt + JWT funciones
│   │   │   └── dependencies.py#   Dependencias FastAPI
│   │   ├── models/usuario.py  #   Modelo ORM Usuario
│   │   └── routes/auth.py     #   Register, Login, Me
│   └── requirements.txt
│
├── Lab_Sesion5/              # Generacion DOCX
│   ├── app/
│   │   ├── main.py            #   FastAPI app
│   │   ├── database.py        #   Conexion PostgreSQL
│   │   ├── models/tesis.py    #   Modelo ORM Tesis
│   │   ├── routes/
│   │   │   ├── tesis.py       #   CRUD tesis
│   │   │   └── documentos.py  #   Descarga DOCX
│   │   ├── schemas/tesis.py   #   Validacion
│   │   └── services/
│   │       └── docx_generator.py  # Generador documentos
│   ├── demos/                 #   6 scripts de demostracion
│   └── requirements.txt
│
├── .gitignore
└── README.md                  # Este archivo
```

---

## Autor

**Milton Vladimir Mamani Calisaya**
Universidad Nacional del Altiplano - Puno
Facultad de Ingenieria Estadistica e Informatica
