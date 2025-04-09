from django import forms
from .models import Libro, AutorLibro, Resena

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro	
        fields = ['titulo', 'descripcion', 'autor_libro', 'fecha_publicacion', 'portada']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del libro'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del libro'}),
            'autor_libro': forms.Select(attrs={'class': 'form-select'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'portada': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'autor_libro': 'Autor del libro',
            'fecha_publicacion': 'Fecha de publicación',
            'portada': 'Portada del libro',
        }
        error_messages = {
            'titulo': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'El título no puede exceder los 200 caracteres.'
            },
            'descripcion': {
                'required': 'Este campo es obligatorio.'
            },
            'autor_libro': {
                'required': 'Este campo es obligatorio.'
            },
            'fecha_publicacion': {
                'required': 'Este campo es obligatorio.'
            },
            'portada': {
                'invalid': 'Formato de imagen no válido.',
                'invalid_image': 'La imagen no es válida.'
            }
        }