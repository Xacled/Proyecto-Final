from django.urls import path
from . import views

app_name = "noticias"

urlpatterns = [
    path("", views.Home_Noticias, name="home_noticias"),
    path("cargar/", views.Cargar_noticia.as_view(), name="cargar_noticia"),
    path("Detalle/<int:pk>", views.Detalle_noticia, name="detalle_noticia"),
    path(
        "Modificar/<int:pk>",
        views.Modificar_noticia.as_view(),
        name="modificar_noticia",
    ),
    path("Borrar/<int:pk>", views.Borrar_noticia.as_view(), name="borrar_noticia"),
    path("likes/<int:pk>", views.megusta, name="megusta"),
]
