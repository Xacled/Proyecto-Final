from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Noticia, Categoria
from .forms import Formulario_Noticia, Formulario_Modificar_Noticia

#CONTROLA SI EL USUARIO ESTA LOGEADO EN UNA VISTA BASADA EN CLASES
from django.contrib.auth.mixins import LoginRequiredMixin
#CONTROLA SI EL USUARIO ESTA LOGEADO EN UNA VISTA BASADA EN FUNCIONEs
from django.contrib.auth.decorators import login_required

#CONTROLA QUE EL USUARIO SEA STAFF VISTA BASADA EN FuNCION
from django.contrib.admin.views.decorators import staff_member_required
#CONTROLA QUE EL USUARIO SEA STAFF PARA VISTA BASADA EN CLASE
from django.contrib.auth.mixins    import UserPassesTestMixin


#Vasta Basada en funciones
def Home_Noticias(request):
	contexto = {}
	cat = Categoria.objects.all()
	contexto['categorias'] = cat

	filtro = request.GET.get('categoria',None)
	if not filtro or filtro == '0':
		todas = Noticia.objects.all()
	else:
		categoria_seleccionada = Categoria.objects.get(pk = filtro)
		todas = Noticia.objects.filter(categoria = categoria_seleccionada)

	
	contexto['noticias'] = todas
	return render(request, 'noticias/home_noticias.html', contexto)

#ACLARACION
'''
si bien en la vista armo un diccionario del tipo
{noticias: todas_noticias, fecha: '28-11-2023'}
en el template resivo variables separadas, una por cada clave, la cual contiene como valor
el valor de la clave
EJ, recibo 2 variales distintas, cuyo nombre es igual a la clave
noticias = todas_noticias
fecha = '28-11-2023'
'''

#VISTA BASADA EN CLASE
class Home_Noticias_clase(ListView):
	model = Noticia
	template_name = 'noticias/home_noticias.html'
	context_object_name = 'noticias'

class Cargar_noticia(CreateView):
	model = Noticia
	template_name = 'noticias/cargar_noticia.html'
	form_class = Formulario_Noticia
	success_url = reverse_lazy('noticias:h_noticias')

class Modificar_noticia(UpdateView):
	model = Noticia
	template_name = 'noticias/modificar_noticia.html'
	form_class = Formulario_Modificar_Noticia
	success_url = reverse_lazy('noticias:h_noticias')

class Borrar_noticia(DeleteView):
	model = Noticia
	success_url = reverse_lazy('noticias:h_noticias')

#ORM
# CONSULTA PARA TRAER TODOS LOS DATOS
# select * from Noticia  SQL
# Noticia.objects.all()   ORM

#CONSuLTA PARA TRAER SOLO UN DATO (POR CLAVE)
# select * from Noticia where id = algo    SQL
# Noticia.objects.get(id = algo)		ORM

#CONSuLTA PARA TRAER SOLO Algunos datos (POR filtro)
# select * from Noticia where categororia = deportes
# Noticia.objects.filter(categoria = deportes)

def Detalle_noticia(request, pk):
	ctx = {}
	n = Noticia.objects.get(pk = pk)
	ctx['noticia'] = n
	return render(request,'noticias/detalle_noticia.html', ctx)