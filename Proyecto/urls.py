"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Home, name="Inicio"),
    path("contacto/", include("apps.contacto.urls"), name="Contacto"),
    # APP NOTICIAS
    path("noticias/", include("apps.noticias.urls")),
    # LOGIN Y LOGOUT
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="usuarios/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "reset_password/",
        views.CustomPasswordResetView.as_view(
            template_name="usuarios/registration/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="usuarios/registration/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="usuarios/registration/password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="usuarios/registration/password_reset_done.html"
        ),
        name="password_reset_complete",
    ),
    # APP USUARIOs
    path("usuarios/", include("apps.usuarios.urls")),
    # APP Comentarios
    path("Comentarios/", include("apps.comentarios.urls")),
    path("acercade/", views.Acercade, name="acercade"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
