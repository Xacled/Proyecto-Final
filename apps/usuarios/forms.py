from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):

    first_name = forms.CharField(
        label='Nombre', 
        max_length=30, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Ingrese su nombre',
            'class': 'form-control'
        })
    )
    
    last_name = forms.CharField(
        label='Apellido', 
        max_length=30, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Ingrese su apellido',
            'class': 'form-control'
        })
    )
    
    username = forms.CharField(
        label='Nombre de usuario', 
        max_length=30, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Ingrese su nombre de usuario',
            'class': 'form-control'
        })
    )
    
    email = forms.EmailField(
        label='Correo electrónico', 
        max_length=254, 
        widget=forms.EmailInput(attrs={
            'placeholder': 'Ingrese su correo electrónico',
            'class': 'form-control'
        })
    )
    
    password1 = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Ingrese su contraseña',
            'class': 'form-control'
        })
    )
    
    password2 = forms.CharField(
        label='Confirmar contraseña', 
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirme su contraseña',
            'class': 'form-control'
        })
    )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]
