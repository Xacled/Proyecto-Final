from django import forms
from .models import Contacto


class Formulario_Contacto(forms.ModelForm):
    nombre = forms.CharField(
        label="nombre",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese su nombre", "class": "form-control"}
        ),
    )
    telefono = forms.IntegerField(
        label="telefono",
        max_value=1000000000000,
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Ingrese su telefono/celular",
                "class": "form-control",
            }
        ),
    )
    email = forms.EmailField(
        label="Correo electrónico",
        max_length=254,
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese su email", "class": "form-control"}
        ),
    )
    RAZON_CHOICES = [
        ("elegir_razon", "Elegir razon"),
        ("problemas_tecnicos", "Problemas técnicos"),
        ("sugerencias", "Sugerencias"),
        ("publicidad", "Publicidad"),
        ("reportar", "Reportar Usuario/Post"),
    ]
    razon = forms.ChoiceField(
        label="razon",
        choices=RAZON_CHOICES,
        widget=forms.Select(
            attrs={"placeholder": "Elegir razon", "class": "form-control"}
        ),
        required=True,
    )
    contenido = forms.CharField(
        label="contentido",
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Contacto
        fields = ["razon", "nombre", "telefono", "email", "contenido"]
