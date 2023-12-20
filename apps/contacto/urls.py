from django.urls import path
from . import views

app_name = "contacto"

urlpatterns = [
    path("", views.Cargar_contacto.as_view(), name="cargar_contacto"),
]
