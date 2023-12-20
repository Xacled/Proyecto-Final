from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Contacto
from .forms import Formulario_Contacto
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

class Cargar_contacto(CreateView):
    model = Contacto
    template_name = "./contacto.html"
    form_class = Formulario_Contacto
    success_url = reverse_lazy("noticias:home_noticias")

    def form_valid(self, form):
        response = super().form_valid(form)

        razon = form.cleaned_data['razon']
        nombre = form.cleaned_data['nombre']
        telefono = form.cleaned_data['telefono']
        email = form.cleaned_data['email']
        contenido = form.cleaned_data['contenido']

        send_mail(
            f'Nuevo formulario enviado: {razon}',
            f' Nombre: {nombre} - Telefono: {telefono} - Emai: {email} - Mensaje: {contenido}',
            email,
            ['blog.info.cambio.climatico@gmail.com'],
            fail_silently=False,
        )
        return response
