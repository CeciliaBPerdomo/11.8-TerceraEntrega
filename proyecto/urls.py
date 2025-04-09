# proyecto/urls.py 
from django.contrib import admin
from django.urls import path, include
from libros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('libros/', include(('libros.urls', 'libros'), namespace='libros')),
]
