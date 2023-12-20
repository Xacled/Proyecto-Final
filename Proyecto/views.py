from django.shortcuts import render
from apps.noticias.models import Noticia
from django.contrib.auth.views import PasswordResetView
from apps.usuarios.models import CustomUser


def Home(request):
    ctx = {}
    noticias_populares = Noticia.objects.order_by("-visitas")[:3]
    ctx["noticias_populares"] = noticias_populares
    return render(request, "home.html", ctx)


def Contacto(request):
    return render(request, "contacto.html")


def Acercade(request):
    return render(request, "info.html")


class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        email = form.cleaned_data["email"]
        if not CustomUser.objects.filter(email=email).exists():
            form.add_error(
                "email",
                "El correo electrónico no está registrado. Por favor, regístrate para crear una cuenta.",
            )
            return self.form_invalid(form)

        return super().form_valid(form)
