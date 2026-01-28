# Manual del Estudiante - Entrega de Trabajos

Guía paso a paso para subir tus laboratorios modificados al repositorio del curso.

---

## Requisitos

- Cuenta en [GitHub](https://github.com) (crear una si no tienes)
- Git instalado → verificar con: `git --version`
- Python 3.8+ → verificar con: `python --version`
- Node.js 18+ → verificar con: `node --version`
- PostgreSQL con base de datos `qillqay` creada

---

## Paso 1: Hacer Fork del repositorio

1. Ir a **https://github.com/vl4dimr/SOFTII**
2. Clic en el botón **Fork** (esquina superior derecha)
3. Esto crea una copia del repositorio en tu cuenta personal

![Fork](https://docs.github.com/assets/cb-43312/mw-1440/images/help/repository/fork-button.webp)

Ahora tendrás: `https://github.com/TU_USUARIO/SOFTII`

---

## Paso 2: Clonar tu Fork

Abre la terminal (Git Bash, CMD o PowerShell) y ejecuta:

```bash
git clone https://github.com/TU_USUARIO/SOFTII.git
cd SOFTII
```

> Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub.

---

## Paso 3: Configurar tu identidad

Solo la primera vez:

```bash
git config user.name "Tu Nombre Completo"
git config user.email "tu_email@ejemplo.com"
```

---

## Paso 4: Crear tu rama de trabajo

Crea una rama con tu nombre (sin espacios, sin tildes):

```bash
git checkout -b alumno/tu-nombre
```

**Ejemplos:**
```bash
git checkout -b alumno/juan-perez
git checkout -b alumno/maria-quispe
git checkout -b alumno/carlos-mamani
```

---

## Paso 5: Modificar los laboratorios

Abre el proyecto en VS Code:

```bash
code .
```

Realiza las modificaciones solicitadas en cada laboratorio. Por ejemplo:

- **Lab 3:** Agregar nuevos endpoints, mejorar el frontend React
- **Lab 4:** Agregar nuevas rutas protegidas
- **Lab 5:** Agregar más secciones al documento DOCX (introducción, objetivos, etc.)

### Estructura de tu trabajo

Trabaja **dentro de las carpetas existentes**:

```
SOFTII/
  Lab_Sesion2/    ← Modifica aquí
  Lab_Sesion3/    ← Modifica aquí (backend + frontend React)
  Lab_Sesion4/    ← Modifica aquí
  Lab_Sesion5/    ← Modifica aquí
```

---

## Paso 5.1: Instalar dependencias

### Backend (Labs 2, 3, 4, 5)

Cada lab tiene su propio `requirements.txt`:

```bash
cd Lab_Sesion3
pip install -r requirements.txt
```

### Frontend React (Solo Lab 3)

El Lab 3 incluye un frontend React en la carpeta `frontend/`:

```bash
cd Lab_Sesion3/frontend
npm install
```

> Esto crea la carpeta `node_modules/` (NO se sube a GitHub, el `.gitignore` la excluye).

---

## Paso 5.2: Ejecutar los laboratorios

### Lab 2 (una sola terminal)

```bash
cd Lab_Sesion2
uvicorn main:app --reload
```
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

### Lab 3 (dos terminales)

**Terminal 1 — Backend:**
```bash
cd Lab_Sesion3
uvicorn app.main:app --reload
```
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

**Terminal 2 — Frontend React:**
```bash
cd Lab_Sesion3/frontend
npx vite
```
- App React: http://localhost:5174

> El frontend React consume la API del backend. Ambos deben estar corriendo al mismo tiempo.

### Lab 4 (una sola terminal)

```bash
cd Lab_Sesion4
uvicorn app.main:app --reload
```
- API: http://localhost:8000
- Probar en Swagger: POST `/auth/register` → POST `/auth/login` → GET `/auth/me` con token

### Lab 5 (una sola terminal)

```bash
cd Lab_Sesion5
uvicorn app.main:app --reload
```
- API: http://localhost:8000
- Probar demos: `python demos/demo1_basico.py` (no requiere servidor)
- Probar descarga: GET `/documentos/tesis/{id}/docx` (requiere servidor)

---

## Paso 5.3: Modificar el Frontend React (Lab 3)

### Estructura del frontend

```
Lab_Sesion3/frontend/
  index.html          ← HTML base (no tocar)
  package.json        ← Dependencias npm (no tocar)
  vite.config.js      ← Config Vite: puerto 5174
  src/
    main.jsx          ← Monta React en el DOM (no tocar)
    App.jsx           ← COMPONENTE PRINCIPAL (modificar aquí)
    api.js            ← Funciones de conexión a la API (modificar si agregas endpoints)
    index.css         ← Estilos visuales (modificar para cambiar diseño)
```

### Archivos clave para modificar

**`src/App.jsx`** — Componente principal con toda la lógica:
- Listado de tesis con tarjetas
- Formulario de creación/edición (modal)
- Búsqueda por título
- Cambio de estado
- Estadísticas

**`src/api.js`** — Funciones que conectan con el backend:
```javascript
// Si agregas un nuevo endpoint en FastAPI, agrega aquí su función fetch:
export async function miFuncion() {
  const res = await fetch("http://localhost:8000/api/mi-endpoint");
  return res.json();
}
```

**`src/index.css`** — Estilos de la aplicación:
- Modificar colores, fuentes, tamaños
- Agregar nuevos estilos para componentes nuevos

### Ejemplo: Agregar un nuevo campo al formulario

**1. Backend** — Agregar campo en `Lab_Sesion3/app/schemas/tesis.py`:
```python
class TesisInput(BaseModel):
    titulo: str
    autor: str
    escuela: str = "Ingenieria de Sistemas"
    asesor: str = ""    # ← NUEVO CAMPO
```

**2. Frontend** — Agregar al estado del formulario en `App.jsx`:
```jsx
const [form, setForm] = useState({
  titulo: "",
  autor: "",
  escuela: "Ingenieria de Sistemas",
  asesor: "",    // ← NUEVO CAMPO
});
```

**3. Frontend** — Agregar input en el formulario JSX en `App.jsx`:
```jsx
<div className="form-group">
  <label>Asesor</label>
  <input
    type="text"
    value={form.asesor}
    onChange={(e) => setForm({ ...form, asesor: e.target.value })}
    placeholder="Nombre del asesor..."
  />
</div>
```

### Hot Reload

Mientras Vite está corriendo (`npx vite`), cada cambio que guardes en los archivos `.jsx` o `.css` se refleja **automáticamente** en el navegador sin recargar la página.

---

## Paso 6: Guardar tus cambios (Commit)

### 6.1 Ver qué archivos modificaste

```bash
git status
```

### 6.2 Agregar los archivos modificados

```bash
git add Lab_Sesion3/
git add Lab_Sesion4/
git add Lab_Sesion5/
```

> Solo agrega las carpetas de los labs que modificaste.

### 6.3 Crear el commit

```bash
git commit -m "Lab 3: Agregar endpoint de búsqueda avanzada - Juan Pérez"
```

**Formato del mensaje:**
```
Lab X: Descripción breve de lo que hiciste - Tu Nombre
```

**Ejemplos:**
```bash
git commit -m "Lab 3: Agregar filtro por fecha en frontend - María Quispe"
git commit -m "Lab 4: Proteger endpoints de tesis con JWT - Carlos Mamani"
git commit -m "Lab 5: Agregar sección de objetivos al DOCX - Ana López"
```

> Puedes hacer varios commits si trabajas en distintos labs.

---

## Paso 7: Subir tu rama a GitHub

```bash
git push origin alumno/tu-nombre
```

**Ejemplo:**
```bash
git push origin alumno/juan-perez
```

La primera vez te pedirá autenticarte en GitHub.

---

## Paso 8: Crear Pull Request (Entrega)

1. Ir a **https://github.com/vl4dimr/SOFTII**
2. Aparecerá un banner amarillo: **"alumno/tu-nombre had recent pushes"**
3. Clic en **Compare & pull request**
4. Llenar el formulario:

**Título:**
```
[Lab X] Tu Nombre Completo
```

**Descripción (copiar y completar):**
```markdown
## Datos del estudiante
- **Nombre:** Tu Nombre Completo
- **Código:** Tu código universitario
- **Escuela:** Ingeniería de Sistemas / Ingeniería Estadística

## Laboratorios modificados
- [ ] Lab 3: (describir qué hiciste)
- [ ] Lab 4: (describir qué hiciste)
- [ ] Lab 5: (describir qué hiciste)

## Capturas de pantalla
(Pegar capturas de la app funcionando)
```

5. Clic en **Create pull request**

---

## Resumen de comandos

```bash
# Solo la primera vez
git clone https://github.com/TU_USUARIO/SOFTII.git
cd SOFTII
git config user.name "Tu Nombre"
git config user.email "tu_email@ejemplo.com"
git checkout -b alumno/tu-nombre

# Cada vez que quieras entregar
git add Lab_Sesion3/ Lab_Sesion4/ Lab_Sesion5/
git commit -m "Lab X: Descripción - Tu Nombre"
git push origin alumno/tu-nombre
# Luego crear Pull Request en GitHub
```

---

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `fatal: not a git repository` | No estás dentro de la carpeta SOFTII | `cd SOFTII` |
| `error: failed to push` | No hiciste fork o la rama no existe | Verificar que hiciste fork y `git checkout -b alumno/tu-nombre` |
| `Author identity unknown` | Falta configurar nombre/email | `git config user.name "Tu Nombre"` |
| `Permission denied` | No tienes acceso al repo original | Verificar que haces push a **tu fork**, no al repo del docente |
| `merge conflict` | Modificaste un archivo que cambió en el original | Pedir ayuda al docente |
| `CORS policy: blocked` | El frontend no puede conectar con el backend | Verificar que el backend esté corriendo en puerto 8000 |
| `ERR_CONNECTION_REFUSED` (React) | El backend no está corriendo | Iniciar backend primero: `uvicorn app.main:app --reload` |
| `npm ERR! missing script` | Estás en la carpeta incorrecta | Ir a `Lab_Sesion3/frontend/` antes de ejecutar npm |
| `Module not found` (React) | Falta instalar dependencias npm | Ejecutar `npm install` en la carpeta `frontend/` |
| React muestra pantalla en blanco | Error en el código JSX | Abrir la consola del navegador (F12) para ver el error |

---

## Reglas importantes

1. **NO** modificar archivos de otros compañeros
2. **NO** subir archivos `.env` (contienen contraseñas)
3. **NO** subir la carpeta `node_modules/` (es muy pesada, el `.gitignore` ya la excluye)
4. **SÍ** incluir capturas de pantalla en el Pull Request
5. **SÍ** probar que tu código funciona antes de entregar
6. **SÍ** escribir mensajes de commit descriptivos

---

## ¿Necesitas ayuda?

- Revisar la documentación de cada lab en el `README.md` principal
- Consultar al docente en clase o por correo
- Ver la guía oficial de GitHub: https://docs.github.com/es/get-started
