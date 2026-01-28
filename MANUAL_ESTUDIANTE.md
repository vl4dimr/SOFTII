# Manual del Estudiante - Entrega de Trabajos

Guía paso a paso para subir tus laboratorios modificados al repositorio del curso.

---

## Requisitos

- Cuenta en [GitHub](https://github.com) (crear una si no tienes)
- Git instalado en tu computadora
- Verificar con: `git --version`

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
  Lab_Sesion3/    ← Modifica aquí
  Lab_Sesion4/    ← Modifica aquí
  Lab_Sesion5/    ← Modifica aquí
```

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
