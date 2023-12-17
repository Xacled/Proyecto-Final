from django.shortcuts import render ,get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import RegistroForm, Formulario_Modificar_Usuario
from .models import CustomUser
# Create your views here.



def Ver_perfil(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'usuarios/perfil.html', {'user': user})

class Registro(CreateView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'usuarios/registro.html'

class Modificar_usuario(UpdateView):
    model = CustomUser
    template_name = 'usuarios/modificar_perfil.html'
    form_class = Formulario_Modificar_Usuario
    success_url = reverse_lazy('noticias:home_noticias')

