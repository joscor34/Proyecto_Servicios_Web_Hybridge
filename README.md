# Aplicación Web con Flask y Flask-RESTful

Proyecto de ejemplo para aprender a construir una aplicación web y una API REST usando Python, Flask y Flask-RESTful.

---

## Estructura del proyecto

```text
Programacion_avanzada/
├── app.py          # Punto de entrada: crea el servidor y lo arranca
├── routes.py       # Administrador de rutas: registra todos los recursos
├── resources.py    # Recursos: lógica de cada endpoint (vistas y API)
└── templates/
    ├── pagina_1.html   # Landing page (ruta /)
    └── pagina_2.html   # Página de preguntas frecuentes (ruta /faq)
```

---

## Requisitos

- Python 3.x
- Flask
- Flask-RESTful

---

## Instalación

### Paso 1 — Crear el entorno virtual

**Mac / Linux**

```bash
python3 -m venv mi-entorno
```

**Windows**

```bash
python -m venv mi-entorno
```

### Paso 2 — Activar el entorno virtual

**Mac / Linux**

```bash
source mi-entorno/bin/activate
```

**Windows (CMD)**

```bash
mi-entorno\Scripts\activate.bat
```

**Windows (PowerShell)**

```bash
mi-entorno\Scripts\Activate.ps1
```

> Si PowerShell bloquea la ejecución, ejecuta primero:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Paso 3 — Instalar las dependencias

```bash
pip install flask flask-restful
```

---

## Ejecutar la aplicación

**Mac / Linux**

```bash
python3 app.py
```

**Windows**

```bash
python app.py
```

El servidor arranca en modo desarrollo en el puerto **8000**.  
Abre tu navegador en: `http://localhost:8000`

---

## Endpoints disponibles

### Páginas web

| Método | Ruta   | Descripción                    |
|--------|--------|--------------------------------|
| GET    | `/`    | Landing page de bienvenida     |
| GET    | `/faq` | Página de preguntas frecuentes |

### API REST

| Método | Ruta       | Descripción                         |
|--------|------------|-------------------------------------|
| GET    | `/primero` | Devuelve una lista de números       |
| GET    | `/segundo` | Devuelve datos de inventario (JSON) |

---

## Arquitectura del proyecto

El proyecto sigue una separación de responsabilidades en tres capas:

```text
app.py  →  routes.py  →  resources.py
```

- **`app.py`** — Crea la instancia de Flask y el motor de la API. Solo arranca el servidor.
- **`routes.py`** — Contiene la clase `AdministradorDeRutas`, que registra cada recurso en su URL correspondiente.
- **`resources.py`** — Contiene una clase por cada endpoint. Cada clase hereda de `Resource` y define métodos `get`, `post`, etc.

### ¿Cómo agregar un nuevo endpoint?

1. Crear una nueva clase en `resources.py` que herede de `Resource`.
2. Definir el método HTTP (`get`, `post`, `put`, `delete`).
3. Registrar la clase en `routes.py` con `aplicacion.add_resource(MiClase, '/mi-ruta')`.

```python
# resources.py
class MiNuevoRecurso(Resource):
    def get(self):
        return {"mensaje": "Hola desde mi nuevo recurso"}

# routes.py
aplicacion.add_resource(MiNuevoRecurso, '/nuevo')
```

---

## Conceptos clave

| Concepto           | Descripción                                           |
|--------------------|-------------------------------------------------------|
| `Flask`            | Framework web que convierte tu PC en un servidor      |
| `Api(app)`         | Motor de Flask-RESTful que gestiona los recursos      |
| `Resource`         | Clase base para definir un endpoint con métodos HTTP  |
| `add_resource`     | Asocia una clase Resource a una URL                   |
| `render_template`  | Convierte un archivo HTML en una respuesta web        |
| `make_response`    | Empaqueta el HTML renderizado como respuesta HTTP     |
