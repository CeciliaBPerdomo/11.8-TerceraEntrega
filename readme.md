<h1 align="center">Blog de libros</h1>
<p align="center"><img src="myAvatar.png"></p>
<p align="center">by Cecilia 💛 Perdomo</p>

--- 
## Base de datos
- 📘 **Módelo 1**: AutorLibro
    - Información sobre los autores de los libros que reseñás.

- 📚 **Módelo 2**: Libro
    - Cada libro tiene un título, descripción, autor, etc.

- ✍️ **Módelo 3**: Reseña
    - Reseñas que recibe cada libro.

- Crea la base de datos: `python manage.py migrate`
    - 🧠 **Tip extra**: Si agregás o modificás un modelo, siempre tenés que correr makemigrations y migrate, así Django sabe qué cambios reflejar en la base de datos.
        - `python manage.py makemigrations` --> (None)
        - `python manage.py migrate`

- Crear usuario administrador: `python manage.py createsuperuser`
- Para borrar toda la base de datos: `rm db.sqlite3`
- **Para cargar info por defecto**: `python manage.py cargar_datos`

---
## Servidor
- Levanta el servidor: `python manage.py runserver`

---

## Instalaciones
- Imágenes para libros: `pip install Pillow`