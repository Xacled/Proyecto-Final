from django import forms
from .models import Comentario


class ComentarioModiciacion(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']