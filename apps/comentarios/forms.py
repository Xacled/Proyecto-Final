from django import forms
from .models import Comentario


class ComentarioModificacion(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["contenido"]
