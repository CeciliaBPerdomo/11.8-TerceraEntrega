# libros/urls.py 
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio de libros

     # Libros
    path('libros/', views.post_libros, name='post_libros'), 
    path('libros/create', views.libros_create, name='libros_create'),  # Crear un nuevo libro

   # Autores    
    path('autores/', views.post_autores, name='post_autores'),
    # path('autores/post/create', views.post_create, name='post_create'),  # Crear un nuevo autor

    # Reseñas
    path('resenas/', views.post_resenas, name='post_resenas'),
]