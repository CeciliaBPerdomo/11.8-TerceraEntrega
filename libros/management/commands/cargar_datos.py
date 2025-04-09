from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from libros.models import AutorLibro, Libro, Resena
from datetime import date

class Command(BaseCommand):
    help = 'Carga autores, libros y reseñas de ejemplo'

    def handle(self, *args, **kwargs):
        # Crear usuarios
        usuario, _ = User.objects.get_or_create(username='Cecilia', defaults={'password': 'ceci1234'})

        # Crear autores
        autor1, _ = AutorLibro.objects.get_or_create(
            nombre='Gabriel García Márquez',
            defaults={
                'biografia': 'Escritor colombiano, autor de "Cien años de soledad" y premio Nobel de Literatura en 1982.',
                'fecha_nacimiento': date(1927, 3, 6)
            }
        )

        autor2, _ = AutorLibro.objects.get_or_create(
            nombre='Jane Austen',
            defaults={
                'biografia': 'Novelista inglesa del siglo XIX, famosa por su aguda crítica social y obras como "Orgullo y prejuicio".',
                'fecha_nacimiento': date(1775, 12, 16)
            }
        )

        autor3, _ = AutorLibro.objects.get_or_create(
            nombre='Sarah J. Maas',
            defaults={
                'biografia': 'Autora estadounidense de fantasía, conocida por sus sagas "Throne of Glass" y "Una corte de rosas y espinas".',
                'fecha_nacimiento': date(1986, 3, 5)
            }
        )

        # Crear libros
        libro1, _ = Libro.objects.get_or_create(
            titulo='Cien años de soledad',
            descripcion='Una novela emblemática del realismo mágico.',
            autor_libro=autor1,
            fecha_publicacion=date(1967, 5, 30)
        )

        libro2, _ = Libro.objects.get_or_create(
            titulo='Orgullo y prejuicio',
            descripcion='Una historia de amor y clase social en la Inglaterra del siglo XIX.',
            autor_libro=autor2,
            fecha_publicacion=date(1813, 1, 28)
        )

        libro3, _ = Libro.objects.get_or_create(
            titulo='Una corte de rosas y espinas',
            descripcion='Primer libro de la saga de fantasía romántica donde Feyre descubre un mundo lleno de magia y peligro.',
            autor_libro=autor3,
            fecha_publicacion=date(2015, 5, 5)
        )

        # Crear reseñas
        Resena.objects.get_or_create(
            libro=libro1,
            usuario=usuario,
            titulo='Una obra maestra',
            contenido='Me encantó cada página de este libro. Inolvidable.',
            puntuacion=5
        )

        Resena.objects.get_or_create(
            libro=libro2,
            usuario=usuario,
            titulo='Un clásico imprescindible',
            contenido='La ironía y la crítica social de Austen son brillantes.',
            puntuacion=4
        )

        Resena.objects.get_or_create(
            libro=libro3,
            usuario=usuario,
            titulo='Fantástico y atrapante',
            contenido='Me encantó el mundo que construye Maas. No podía dejar de leer.',
            puntuacion=5
        )

        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente'))
