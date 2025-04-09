# libros/views.py 
from django.shortcuts import render
from .models import Libro

# Create your views here.
def index(request):
    return render(request, 'libros/index.html')


def post_libros(request):
    # Obtener el valor de la búsqueda desde la URL
    busqueda = request.GET.get('busqueda', None)
    if busqueda:
        post_libros = Libro.objects.filter(titulo__icontains=busqueda)
    else:
        # Obtener todas las publicaciones de la base de datos
        post_libros = Libro.objects.all()
    return render(request, 'libros/libros.html', context={'libros': post_libros})

def post_create(request):
    # Lógica para crear un libro
    return render(request, 'libros/post_create.html')