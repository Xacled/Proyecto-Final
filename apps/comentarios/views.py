from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect
from django.views.generic import DeleteView, UpdateView
from apps.noticias.models import Noticia
from .models import Comentario
from django.urls import reverse_lazy
from .forms import ComentarioModificacion
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def Agregar_Comentario(request, pk):
    contenido = request.POST.get("comentario", None)
    noticia = get_object_or_404(Noticia, pk=pk)
    usuario = request.user
    Comentario.objects.create(contenido=contenido, usuario=usuario, noticia=noticia)
    return HttpResponseRedirect(
        reverse_lazy("noticias:detalle_noticia", kwargs={"pk": pk})
    )


class BorrarComentario(LoginRequiredMixin, DeleteView):
    model = Comentario

    def get_success_url(self):
        noticia_pk = self.object.noticia.pk
        return reverse_lazy("noticias:detalle_noticia", kwargs={"pk": noticia_pk})

    def delete(self, request, *args, **kwargs):
        comentario = self.get_object()
        if request.user == comentario.usuario:
            messages.success(request, "Comentario eliminado exitosamente.")
            return super().delete(request, *args, **kwargs)
        else:
            messages.error(request, "No tienes permisos para eliminar este comentario.")
            return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name="dispatch")
class ModificaComentario(UpdateView):
    model = Comentario
    form_class = ComentarioModificacion
    template_name = "comentarios/modificar.html"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "noticias:detalle_noticia", kwargs={"pk": self.object.noticia.pk}
        )

    def dispatch(self, request, *args, **kwargs):
        comentario = self.get_object()
        if request.user != comentario.usuario:
            messages.error(
                request, "No tienes permisos para modificar este comentario."
            )
            return redirect("noticias:detalle_noticia", pk=comentario.noticia.pk)
        return super().dispatch(request, *args, **kwargs)
