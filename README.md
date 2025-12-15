## TuPrimeraPagina_AdrianOrue

Este proyecto es una web en Django que simula un blog con gestión de autores, posts y comentarios.

---

## Estructura del proyecto

- `TuPrimeraPagina_AdrianOrue/` → Configuración principal de Django  
  - `settings.py` → configuraciones del proyecto  
  - `urls.py` → URLs principales del proyecto  
  - `wsgi.py` / `asgi.py` → archivos de despliegue  
- `blog/` → App principal del proyecto  
  - `models.py` → clases `Author`, `Post`, `Comment`  
  - `forms.py` → formularios para crear cada modelo  
  - `views.py` → funciones que controlan la lógica de la web  
  - `urls.py` → rutas de la app (`author/`, `post/`, `comment/`, `search/`)  
  - `templates/` → archivos HTML, usando herencia de `base.html`  
- `manage.py` → script principal de Django  
- `db.sqlite3` → base de datos local (SQLite)

---

## Instrucciones para probar el proyecto

1. **Instalar dependencias**

```bash
pip install django

2. Levantar el servidor de desarrollo

python manage.py runserver

3. Abrir la web en el navegador

Panel de administración de Django: http://127.0.0.1:8000/admin/

Crear un autor: http://127.0.0.1:8000/blog/author/

Crear un post: http://127.0.0.1:8000/blog/post/

Crear un comentario: http://127.0.0.1:8000/blog/comment/

Buscar posts: http://127.0.0.1:8000/blog/search/

4. Notas sobre las funcionalidades

Todos los formularios usan CSRF token para seguridad.

Los templates HTML usan herencia desde base.html.

Las URLs y vistas están claramente separadas en blog/urls.py y blog/views.py.

La búsqueda de posts funciona por título y muestra resultados en la misma página.

---

Resumen de funcionalidades

Crear Autor → Formulario que registra autores en la base de datos

Crear Post → Formulario que registra posts relacionados a un autor

Crear Comment → Formulario que registra comentarios asociados a un post

Buscar Post → Formulario que permite buscar posts por título