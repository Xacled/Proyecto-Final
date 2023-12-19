from django.shortcuts import HttpResponseRedirect
from django.views.generic import DeleteView, UpdateView
from apps.noticias.models import Noticia
from .models import Comentario
from django.urls import reverse_lazy
from .forms import ComentarioModiciacion
from django.contrib import messages

def Agregar_Comentario(request,pk):

	contenido = request.POST.get('comentario',None)

	noticia = Noticia.objects.get(pk = pk)
	usuario = request.user
	Comentario.objects.create(contenido = contenido, usuario = usuario, noticia = noticia)

	return HttpResponseRedirect(reverse_lazy('noticias:detalle_noticia', kwargs = {'pk':pk}))

class BorrarComentario(DeleteView):
    model = Comentario

    def get_success_url(self):
        noticia_pk = self.object.noticia.pk
        return reverse_lazy('noticias:detalle_noticia', kwargs={'pk': noticia_pk})

    def delete(self, request, *args, **kwargs):
        comentario = self.get_object()

        # Verificar que el usuario que realiza la acción sea el propietario del comentario
        if request.user == comentario.usuario:
            messages.success(request, 'Comentario eliminado exitosamente.')
            return super().delete(request, *args, **kwargs)
        else:
            messages.error(request, 'No tienes permisos para eliminar este comentario.')
            return HttpResponseRedirect(self.get_success_url())

class ModificaComentario(UpdateView):
	model = Comentario
	form_class = ComentarioModiciacion
	template_name = 'comentarios/modificar.html'
	def get_success_url(self):         
		return reverse_lazy('noticias:detalle_noticia',kwargs={'pk': self.object.noticia.pk})