# libros/urls.py 
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio de libros
    path('libros/', views.post_libros, name='post_libros'),  # Lista de libros
   # path('libros/post/create', views.post_create, name='post_create'),  # Crear un nuevo libro
]