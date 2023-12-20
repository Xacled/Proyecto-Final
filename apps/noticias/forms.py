from django import forms
from .models import Noticia


class Formulario_Noticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "contenido", "imagen", "categoria"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "contenido": forms.Textarea(attrs={"class": "form-control"}),
            "imagen": forms.FileInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-control"}),
        }



class Formulario_Modificar_Noticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "contenido", "imagen", "categoria"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "contenido": forms.Textarea(attrs={"class": "form-control"}),
            "imagen": forms.FileInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-control"}),
        }

