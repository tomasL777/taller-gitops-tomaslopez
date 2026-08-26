# Sistema de Gestión Académica - MVC FastAPI + DevOps

Proyecto base desarrollado con **FastAPI**, **SQLModel**, motor de plantillas **Jinja2** y un módulo de cálculo de calificaciones en **Python**, preparado para la evaluación de estrategias de ramificación en Git, Integración Continua (CI) y pruebas automatizadas con **pytest**.

---

## Guía de Inicio Rápido en Local

Sigue estos pasos para poner a punto y ejecutar el proyecto en tu entorno local:

### 1. Crear y activar el entorno virtual

* **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

* **En Windows (CMD / PowerShell):**
  ```powershell
  python -m venv venv
  venv\Scripts\activate
  ```

### 2. Instalar dependencias

Asegúrate de tener `pip` actualizado e instala las librerías del proyecto:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Ejecutar el servidor web de desarrollo

Inicia el servidor local con `uvicorn`:

```bash
uvicorn main:app --reload
```

Abre tu navegador en:
* Aplicación web: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Documentación interactiva Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Ejecución de Pruebas Unitarias y Cobertura

Para ejecutar las pruebas y validar el porcentaje de cobertura de código:

* **Ejecutar pruebas en consola:**
  ```bash
  pytest -v
  ```

* **Ejecutar pruebas con reporte de cobertura detallado:**
  ```bash
  pytest --cov=. --cov-report=term-missing
  ```

* **Validar umbral mínimo de cobertura (80% requerido en CI):**
  ```bash
  pytest --cov=. --cov-report=term-missing --cov-fail-under=80
  ```

---

## Estructura del Proyecto

```
src_base/
├── .gitignore          # Reglas de exclusión para Git (cache, db, venv)
├── database.py         # Configuración y conexión a SQLite
├── models.py           # Modelos de datos SQLModel (Estudiante, Nota)
├── main.py             # Controladores y rutas de la aplicación web
├── logica.py           # Reto de lógica de calificaciones (calcular_estadisticas_notas)
├── test_main.py        # Suite de pruebas unitarias automatizadas
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Guía de uso y comandos
└── templates/          # Vistas HTML con Jinja2
    ├── base.html       # Plantilla base con Bootstrap 5
    └── index.html      # Directorio y formulario de estudiantes
```
