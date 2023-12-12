from django import forms
from .models import Noticia, Comentario


class Formulario_Noticia(forms.ModelForm):

	class Meta:
		model = Noticia
		fields = ['titulo','contenido','imagen','categoria']

class Formulario_Modificar_Noticia(forms.ModelForm):

	class Meta:
		model = Noticia
		fields = ['titulo','contenido','imagen','categoria']


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']