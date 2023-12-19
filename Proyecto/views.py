from django.shortcuts import render
from apps.noticias.models import Noticia

def Home(request):
	ctx = {}
	noticias_populares = Noticia.objects.order_by('-visitas')[:3]  # Obtén las 5 noticias más populares
	ctx['noticias_populares'] = noticias_populares
	return render(request, 'home.html', ctx)


def Contacto(request):

	return render(request,'contacto.html')

def Acercade(request):

	return render(request,'info.html')

