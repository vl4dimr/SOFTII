# GUIA DOCENTE - SESION 5
## Generacion de Documentos DOCX con python-docx
### 7:00 AM - 9:30 AM (2.5 horas)

---

## SLIDE 1-2: PORTADA Y AGENDA (3 min)

**Decir:**
> "Ayer aseguramos la API con JWT. Hoy conectamos con el objetivo principal de Qillqay: generar documentos Word automaticamente."

---

## SLIDE 3: EL OBJETIVO QILLQAY (5 min)

**Decir:**
> "El problema real: estudiantes pasan horas formateando tesis. Errores de margenes, fuentes, la biblioteca rechaza. Qillqay resuelve esto."

**Mostrar ejemplo:**
- Tesis mal formateada (margenes incorrectos)
- Tesis bien formateada (generada automaticamente)

---

## SLIDE 4: QUE ES PYTHON-DOCX (8 min)

**Decir:**
> "Un archivo .docx no es mas que un ZIP con archivos XML. python-docx abstrae esa complejidad."

**Demostrar:**
```bash
# Mostrar que un docx es un zip
# Renombrar un .docx a .zip y abrirlo
copy documento.docx documento.zip
# Explorar contenido: word/document.xml, styles.xml, etc.
```

**Instalar:**
```bash
pip install python-docx
```

---

## SLIDE 5: CREAR DOCUMENTO BASICO (5 min)

**Explicar los metodos principales:**
- `Document()` - Crear o abrir
- `add_heading()` - Titulos
- `add_paragraph()` - Parrafos
- `save()` - Guardar

---

## SLIDE 6: DEMO 1 - DOCUMENTO BASICO (5 min)

**Ejecutar en vivo:**
```bash
python demos/demo1_basico.py
```

**Abrir `demos/demo1_resultado.docx` en Word para mostrar resultado.**

**Preguntar a la clase:**
> "Que metodo usamos para agregar un titulo? Y un parrafo?"

---

## SLIDE 7: FORMATO DE TEXTO - RUNS (5 min)

**Decir:**
> "Un parrafo puede tener multiples 'runs'. Cada run tiene su propio formato. Asi podemos tener negrita, cursiva y normal en el mismo parrafo."

---

## SLIDE 8: DEMO 2 - FORMATO DE TEXTO (5 min)

**Ejecutar en vivo:**
```bash
python demos/demo2_formato.py
```

**Abrir `demos/demo2_resultado.docx` en Word.**

**Senalar:**
- Texto normal, negrita, cursiva, subrayado en un mismo parrafo
- Texto grande (24pt) en otro parrafo
- Cada "run" mantiene su formato independiente

---

## SLIDE 9: CONFIGURAR PAGINA - MARGENES UNAP (5 min)

**Decir:**
> "El formato de tesis UNAP tiene margenes especificos. El izquierdo es 4cm para el empaste. Esto es lo que mas rechazan en biblioteca."

**Enfatizar:**
- `Cm(4)` para margen izquierdo (empaste)
- `section = doc.sections[0]` para acceder a la configuracion de pagina

---

## SLIDE 10: DEMO 3 - MARGENES UNAP (5 min)

**Ejecutar en vivo:**
```bash
python demos/demo3_margenes.py
```

**Abrir `demos/demo3_resultado.docx` en Word.**

**Mostrar:**
1. Activar la regla (Vista > Regla)
2. Verificar margen izquierdo de 4cm
3. Verificar margen derecho de 2.5cm
4. Texto justificado con Times New Roman 12pt

---

## SLIDE 11: CREAR TABLAS (5 min)

**Decir:**
> "Las tablas son esenciales para la pagina de jurados, tabla de contenidos y lista de figuras."

**Explicar:**
- `add_table(rows, cols)` - Crear tabla
- `tabla.style = "Table Grid"` - Estilo con bordes
- Acceder a celdas: `tabla.rows[i].cells[j].text`

---

## SLIDE 12: DEMO 4 - TABLAS (5 min)

**Ejecutar en vivo:**
```bash
python demos/demo4_tablas.py
```

**Abrir `demos/demo4_resultado.docx` en Word.**

**Senalar:**
- Tabla con bordes (Table Grid)
- 4 jurados con cargo y nombre
- Espacio para firma

---

## SLIDE 13: PLANTILLAS CON VARIABLES (8 min)

**Decir:**
> "En vez de generar todo desde cero, podemos usar una plantilla Word con marcadores {{VARIABLE}} y reemplazarlos con datos reales."

**Explicar el patron:**
1. Crear plantilla en Word con `{{TITULO}}`, `{{AUTOR}}`, etc.
2. Abrir con python-docx
3. Recorrer parrafos buscando marcadores
4. Reemplazar con datos reales

---

## SLIDE 14: SERVICIO GENERADOR DE TESIS (8 min)

**Decir:**
> "Ahora juntamos todo en un servicio reutilizable. Este archivo va en `app/services/docx_generator.py`."

**Explicar la arquitectura:**
- Funcion `configurar_margenes_unap()` - Reutilizable
- Funcion `generar_portada()` - Centrado con formato UNAP
- Funcion `generar_tesis()` - Orquesta todo

---

## SLIDE 15: DEMO 5 - PORTADA UNAP COMPLETA (8 min)

**Ejecutar en vivo:**
```bash
python demos/demo5_portada_unap.py
```

**Abrir `demos/demo5_resultado.docx` en Word.**

**Mostrar:**
1. Portada completa con universidad, facultad, escuela
2. Titulo de la tesis centrado
3. Nombre del autor
4. Titulo profesional
5. Lugar y fecha
6. Pagina de jurados con tabla

**Preguntar:**
> "Se ve igual a una portada de tesis real? Que le faltaria?"

---

## SLIDE 16: ENDPOINT PARA DESCARGAR DOCX (10 min)

**Decir:**
> "Ahora conectamos el generador con la API. El endpoint recibe un ID de tesis, la busca en la base de datos, genera el DOCX y lo retorna como descarga."

**Conceptos clave:**
- `BytesIO()` - Guardar en memoria, NO en disco
- `buffer.seek(0)` - Volver al inicio despues de escribir
- `StreamingResponse` - Retornar archivo como descarga
- `media_type` - Tipo MIME para Word

**Preguntar:**
> "Por que usamos BytesIO en vez de guardar en disco?"
> R: Porque no queremos llenar el servidor de archivos temporales.

---

## SLIDE 17: ESTRUCTURA DEL PROYECTO (3 min)

**Mostrar la estructura completa del Lab 5.**

**Senalar los archivos nuevos:**
- `services/docx_generator.py` - Logica de generacion
- `routes/documentos.py` - Endpoints de descarga
- `demos/` - Scripts de demostracion

---

## SLIDE 18: DEMO 6 - FLUJO COMPLETO API (10 min)

**Paso 1 - Iniciar servidor:**
```bash
uvicorn app.main:app --reload
```

**Paso 2 - En otra terminal:**
```bash
python demos/demo6_api.py
```

**Mostrar el output:**
- Tesis creada en BD
- Preview con datos
- DOCX descargado (35,607 bytes)

**Tambien mostrar en Swagger:**
1. Abrir http://localhost:8000/docs
2. Crear tesis con POST /api/tesis
3. Descargar con GET /documentos/tesis/{id}/docx
4. El navegador descarga el archivo automaticamente

---

## SLIDE 19: CIERRE (5 min)

**Resumen:**
> "Ahora pueden generar documentos Word desde la API. El estudiante llena datos, el sistema genera el documento formateado correctamente."

**Tarea:**
1. Revisar el servicio docx_generator.py
2. Probar el endpoint /documentos/tesis/{id}/docx
3. Agregar mas secciones al documento (introduccion, objetivos)
4. Push a GitHub

**Proxima sesion:**
> "Manana: Validador de Formato. Analizaremos PDFs de tesis para detectar errores de formato automaticamente."

---

## CHECKLIST RAPIDO

Antes de clase:
- [ ] python-docx instalado (`pip install python-docx`)
- [ ] PostgreSQL corriendo con BD `qillqay`
- [ ] Word o LibreOffice para mostrar resultados
- [ ] Lab_Sesion5 con todos los archivos
- [ ] Probar los 6 demos antes de clase

Durante clase:
- [ ] Ejecutar cada demo despues de la teoria
- [ ] Abrir cada .docx generado para verificar
- [ ] Mostrar margenes con la regla de Word
- [ ] Probar descarga desde Swagger (Demo 6)

Al cerrar:
- [ ] Verificar que entienden BytesIO (memoria vs disco)
- [ ] Verificar que entienden StreamingResponse
- [ ] Recordar: `buffer.seek(0)` despues de `doc.save(buffer)`

---

## DEMOS DISPONIBLES

| Demo | Script | Que genera |
|------|--------|------------|
| 1 | `demos/demo1_basico.py` | Documento con titulo y parrafo |
| 2 | `demos/demo2_formato.py` | Texto con negrita, cursiva, subrayado |
| 3 | `demos/demo3_margenes.py` | Pagina con margenes UNAP (4cm izq) |
| 4 | `demos/demo4_tablas.py` | Tabla de jurados calificadores |
| 5 | `demos/demo5_portada_unap.py` | Portada UNAP completa + jurados |
| 6 | `demos/demo6_api.py` | Flujo completo: crear tesis + descargar DOCX |

---

## FRASES CLAVE

- "Un DOCX es un ZIP con archivos XML"
- "Un parrafo tiene multiples runs con diferente formato"
- "Margen izquierdo 4cm para empaste"
- "BytesIO guarda en memoria, no en disco"
- "StreamingResponse permite descargar archivos"
- "buffer.seek(0) para volver al inicio antes de enviar"

---

## ERRORES COMUNES

| Error | Causa | Solucion |
|-------|-------|----------|
| `ModuleNotFoundError: No module named 'docx'` | Falta instalar | `pip install python-docx` (no `docx`) |
| Documento vacio al descargar | Falta `buffer.seek(0)` | Agregar `buffer.seek(0)` despues de `doc.save(buffer)` |
| Margenes no se aplican | Usar `sections[0]` | `section = doc.sections[0]` antes de configurar |
| Tabla sin bordes | Falta estilo | `tabla.style = "Table Grid"` |
