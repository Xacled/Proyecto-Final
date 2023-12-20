from django.shortcuts import render
from apps.noticias.models import Noticia
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse
from django.http import HttpResponseRedirect
from apps.usuarios.models import CustomUser  # Ajusta esta importación


def Home(request):
    return render(request, "home.html")


def Contacto(request):
    return render(request, "contacto.html")


def Acercade(request):
    return render(request, "info.html")


# en views.py de tu aplicación principal


class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        # Verifica si el correo electrónico está registrado
        email = form.cleaned_data["email"]
        if not CustomUser.objects.filter(email=email).exists():  # Ajusta esta línea
            # Si no está registrado, redirige a una página personalizada de error
            form.add_error(
                "email",
                "El correo electrónico no está registrado. Por favor, regístrate para crear una cuenta.",
            )
            return self.form_invalid(form)

        # Si el correo está registrado, continúa con la lógica predeterminada
        return super().form_valid(form)
