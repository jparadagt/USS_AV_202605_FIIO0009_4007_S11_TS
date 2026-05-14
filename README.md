# USS_AV_202605_FIIO0009_4007_S11_TS
Taller Sumativo – Individual: Taller MVT: construyendo tu primera app en Django

### Asignatura
XXXX

### Profesor
XXXX

### Alumno
Jonathan Parada G.

# Tienda Project - Django MVT

Proyecto desarrollado con Django utilizando la arquitectura MVT (Modelo - Vista - Template).

El sistema permite visualizar un catálogo de productos almacenados en una base de datos SQLite utilizando el ORM de Django.

---

# Tecnologías utilizadas

- Python 3
- Django
- SQLite
- Bootstrap 5

---

# Estructura del proyecto

```text
tienda_project/
│
├── catalogo/
│   ├── fixtures/
│   │   └── productos.json
│   ├── migrations/
│   ├── templates/
│   │   └── catalogo/
│   │       └── lista_productos.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── tienda_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

# Requisitos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.x
- pip

Verificar instalación:

```bash
python --version
pip --version
```

---

# Instalación del proyecto

## 1. Clonar repositorio

```bash
git clone <URL_REPOSITORIO>
```

## 2. Ingresar al proyecto

```bash
cd tienda_project
```

---

# Crear entorno virtual

## Linux / Mac

```bash
python3 -m venv venv
```

## Windows

```bash
python -m venv venv
```

---

# Activar entorno virtual

## Linux / Mac

```bash
source venv/bin/activate
```

## Windows

```bash
venv\Scripts\activate
```

---

# Instalar dependencias

```bash
pip install django
```

---

# Ejecutar migraciones

Crear migraciones:

```bash
python manage.py makemigrations
```

Aplicar migraciones:

```bash
python manage.py migrate
```

---

# Cargar datos de prueba

El proyecto incluye fixtures con productos de ejemplo.

Ejecutar:

```bash
python manage.py loaddata productos
```

Esto cargará automáticamente productos en la base de datos SQLite.

---

# Levantar servidor de desarrollo

```bash
python manage.py runserver
```

---

# Acceder al sistema

Abrir navegador en:

```text
http://127.0.0.1:8000/productos/
```

---

# Funcionalidades implementadas

- Arquitectura MVT
- Modelo Producto
- ORM Django
- Migraciones
- Templates HTML
- Bootstrap 5
- Tabla de productos
- Persistencia SQLite
- Fixtures JSON

---

# Modelo Producto

El modelo contiene:

| Campo | Tipo |
|---|---|
| nombre | CharField |
| precio | DecimalField |
| stock | PositiveIntegerField |

---

# Flujo MVT implementado

```text
Request
   ↓
URL
   ↓
View
   ↓
Modelo ORM
   ↓
Template HTML
   ↓
Response
```

---

# Autor

Proyecto académico desarrollado utilizando Django y arquitectura MVT.