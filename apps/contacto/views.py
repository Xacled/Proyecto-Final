from django.shortcuts import render
from .models import Contacto
from .forms import Formulario_Contacto
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.
class Cargar_contacto(CreateView):
    model = Contacto
    template_name = "./contacto.html"
    form_class = Formulario_Contacto
    success_url = reverse_lazy("noticias:home_noticias")
