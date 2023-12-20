from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("Registro/", views.Registro.as_view(), name="registro_usuario"),
    path("<str:username>/", views.Ver_perfil, name="ver_perfil"),
    path(
        "Modificar/<int:pk>/",
        views.Modificar_usuario.as_view(),
        name="modificar_perfil",
    ),
]
