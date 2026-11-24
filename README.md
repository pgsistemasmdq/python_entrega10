
# Preentrega 10 - CRUD de Posts con Imágenes en Django

## Descripción

Proyecto desarrollado para el curso de Python de Coderhouse.

Esta entrega continúa el desarrollo del blog Django de los módulos anteriores, conservando el modelo Post, el ORM, las migraciones, los templates y el panel de administración.

En esta etapa se incorpora un sistema CRUD completo para gestionar publicaciones desde el sitio web, utilizando formularios ModelForm y permitiendo cargar imágenes.

El proyecto incluye una base de datos SQLite con publicaciones de demostración e imágenes asociadas.

## Funcionalidades

El blog permite:

- Listar publicaciones.
- Ver el detalle de cada post.
- Crear nuevas publicaciones.
- Editar publicaciones existentes.
- Eliminar publicaciones con confirmación.
- Cargar imágenes en los posts.
- Crear publicaciones sin imagen.
- Administrar publicaciones desde Django Admin.
- Diferenciar publicaciones publicadas, borradores y archivadas.

Las publicaciones visibles en el listado público se consultan mediante el ORM de Django.

## Tecnologías utilizadas

- Python 3
- Django 5.2
- SQLite
- HTML5
- CSS3
- Django Templates
- Django ModelForm
- Pillow
- Git y GitHub

## Estructura del proyecto

```text
blog_django/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
├── .gitignore
│
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── posts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── templates/
│   │   └── posts/
│   └── static/
│       └── posts/
│           └── css/
│
└── media/
    └── posts/
```

## Instalación

### 1. Clonar el repositorio

```powershell
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta del proyecto donde se encuentra `manage.py`.

### 2. Crear el entorno virtual

```powershell
py -m venv .venv
```

### 3. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

Este comando instala Django y Pillow.

### 5. Verificar la configuración

```powershell
python manage.py check
```

### 6. Aplicar las migraciones pendientes

```powershell
python manage.py migrate
```

El repositorio incluye una base SQLite con publicaciones de ejemplo.

El comando `migrate` permite aplicar cualquier migración pendiente sin eliminar los posts existentes.

### 7. Ejecutar el servidor

```powershell
python manage.py runserver
```

Abrir en el navegador:

**Listado de publicaciones:**

http://127.0.0.1:8000/posts/

**Panel de administración:**

http://127.0.0.1:8000/admin/

Para detener el servidor utilizar `Ctrl + C`.

## Base de datos SQLite

Para facilitar la evaluación de la entrega, se incluye el archivo:

`db.sqlite3`

Esta base de datos contiene publicaciones de demostración con distintos autores, títulos, contenidos y estados.

Las publicaciones están relacionadas con temas tecnológicos:

- Inteligencia Artificial.
- Desarrollo de Software.
- PostgreSQL y bases de datos.
- Ciberseguridad.
- Computación en la nube.

De esta manera, al clonar el repositorio y ejecutar Django, las publicaciones ya estarán disponibles sin necesidad de cargarlas nuevamente.

La base se utiliza únicamente para fines educativos y contiene datos de prueba.

## Imágenes de las publicaciones

El modelo Post incorpora el campo:

```python
imagen = models.ImageField(
    upload_to="posts/",
    null=True,
    blank=True
)
```

Este campo permite asociar una imagen opcional a cada publicación.

En `blog_project/settings.py` se configuró:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

Los archivos se almacenan en:

```text
media/posts/
```

El repositorio incluye las imágenes de las publicaciones de ejemplo.

Django permite visualizar estos archivos durante el desarrollo mediante la configuración de las rutas media.

## Operaciones CRUD

### Crear un post

1. Ingresar a `/posts/`.
2. Seleccionar **Nuevo post**.
3. Completar título, contenido, autor y estado.
4. Seleccionar una imagen si se desea.
5. Guardar la publicación.

### Ver un post

Desde el listado, seleccionar una publicación.

Se mostrará su página de detalle con:

- Título.
- Contenido.
- Autor.
- Estado.
- Imagen, si existe.

### Editar un post

1. Abrir el detalle de una publicación.
2. Seleccionar **Editar**.
3. Modificar los campos necesarios.
4. Reemplazar la imagen si corresponde.
5. Guardar los cambios.

### Eliminar un post

1. Abrir la publicación.
2. Seleccionar **Eliminar**.
3. Confirmar la eliminación desde la pantalla correspondiente.

La eliminación requiere confirmación previa.

## Archivos fundamentales

- `posts/models.py`: define el modelo Post y su campo imagen.
- `posts/migrations/0002_post_imagen.py`: migración que incorpora el campo imagen.
- `posts/forms.py`: formulario PostForm basado en ModelForm.
- `posts/views.py`: vistas para listar, ver detalle, crear, editar y eliminar publicaciones.
- `posts/urls.py`: rutas de las operaciones del blog.
- `posts/admin.py`: administración de publicaciones.
- `posts/templates/posts/`: templates HTML.
- `posts/static/posts/css/`: estilos del sitio.
- `blog_project/settings.py`: configuración general y archivos media.
- `blog_project/urls.py`: rutas principales y media durante el desarrollo.
- `requirements.txt`: dependencias Django y Pillow.
- `db.sqlite3`: base de datos con publicaciones de demostración.
- `media/posts/`: imágenes asociadas a las publicaciones.

## Formularios e imágenes

Se utiliza una clase `PostForm` que hereda de `forms.ModelForm`.

El formulario permite trabajar con:

- titulo
- contenido
- autor
- estado
- imagen

Para permitir la carga de imágenes, el formulario HTML utiliza:

```html
enctype="multipart/form-data"
```

Las vistas procesan los archivos enviados utilizando `request.FILES`.

## Pruebas

Para ejecutar las pruebas automatizadas:

```powershell
python manage.py test
```

También se realizaron pruebas manuales de las siguientes funcionalidades:

1. Visualización del listado de publicaciones.
2. Acceso al detalle de cada post.
3. Creación de publicaciones con imagen.
4. Creación de publicaciones sin imagen.
5. Edición de publicaciones.
6. Reemplazo de imágenes.
7. Eliminación con confirmación.
8. Visualización de imágenes en el navegador.
9. Filtrado de publicaciones según su estado.

## Administración de Django

El modelo Post se encuentra registrado en el panel administrativo.

Para crear un administrador local, si fuera necesario:

```powershell
python manage.py createsuperuser
```

Después ingresar a:

http://127.0.0.1:8000/admin/

## Control de versiones

El proyecto utiliza Git y GitHub.

Se incluyen en el repositorio:

- Código fuente del proyecto Django.
- Templates HTML y estilos CSS.
- Archivos de migraciones.
- Archivo requirements.txt.
- Archivo README.md.
- Base SQLite con datos de demostración.
- Imágenes de las publicaciones de ejemplo.

Se excluyen mediante `.gitignore`:

- Entornos virtuales.
- Archivos temporales de Python.
- Variables de entorno privadas.
- Archivos temporales de SQLite.
- Configuraciones locales de VS Code.

## Alcance de la entrega

En esta Preentrega 10, el CRUD es público de acuerdo con los contenidos trabajados en el módulo.

La autenticación de usuarios, los perfiles y la protección de las operaciones de creación, edición y eliminación se incorporarán en la Preentrega 11.

El proyecto está destinado exclusivamente a desarrollo local y evaluación académica.

**No debe utilizarse como aplicación pública de producción sin incorporar autenticación, permisos y medidas adicionales de seguridad.**

## Autor

Proyecto desarrollado para el curso de Python de Coderhouse.

**Preentrega 10 - CRUD de Posts con Imágenes en Django.**
