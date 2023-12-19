from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Noticia, Categoria
from .forms import Formulario_Noticia, Formulario_Modificar_Noticia
from apps.comentarios.models import Comentario


# CONTROLA SI EL USUARIO ESTA LOGEADO EN UNA VISTA BASADA EN CLASES
from django.contrib.auth.mixins import LoginRequiredMixin
# CONTROLA SI EL USUARIO ESTA LOGEADO EN UNA VISTA BASADA EN FUNCIONEs
from django.contrib.auth.decorators import login_required

# CONTROLA QUE EL USUARIO SEA STAFF VISTA BASADA EN FuNCION
from django.contrib.admin.views.decorators import staff_member_required
# CONTROLA QUE EL USUARIO SEA STAFF PARA VISTA BASADA EN CLASE
from django.contrib.auth.mixins import UserPassesTestMixin

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from colorthief import ColorThief

def Home_Noticias(request):
    contexto = {}

    # Obtén la lista de categorías
    contexto['categorias'] = Categoria.objects.all()

    # Obtén el filtro de categoría y orden desde la URL
    filtro = request.GET.get('categoria', '0')
    orden = request.GET.get('orden', '-creado')
    busqueda = request.GET.get('q', '')

    # Filtra las noticias según la categoría seleccionada
    if filtro and filtro != '0':
        categoria_seleccionada = Categoria.objects.get(pk=filtro)
        todas = Noticia.objects.filter(categoria=categoria_seleccionada)
    else:
        todas = Noticia.objects.all()

    # Aplica la búsqueda en el título y el contenido
    if busqueda:
        todas = todas.filter(titulo__icontains=busqueda) | todas.filter(contenido__icontains=busqueda)

    # Ordena las noticias según el criterio de orden seleccionado
    todas = todas.order_by(orden)

    # Implementar paginación
    paginator = Paginator(todas, 5)  
    page = request.GET.get('page')

    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número entero, muestra la primera página
        noticias = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, muestra la última página disponible
        noticias = paginator.page(paginator.num_pages)

    contexto['noticias'] = noticias
    return render(request, 'noticias/home_noticias.html', contexto)

class Cargar_noticia(CreateView):
    model = Noticia
    template_name = 'noticias/cargar_noticia.html'
    form_class = Formulario_Noticia
    success_url = reverse_lazy('noticias:home_noticias')


class Modificar_noticia(UpdateView):
    model = Noticia
    template_name = 'noticias/modificar_noticia.html'
    form_class = Formulario_Modificar_Noticia
    success_url = reverse_lazy('noticias:home_noticias')


class Borrar_noticia(DeleteView):
    model = Noticia

    def get_success_url(self):
        return reverse_lazy('noticias:home_noticias')

    def delete(self, request, *args, **kwargs):
        noticia = self.get_object()

        # Verificar que el usuario que realiza la acción sea el propietario de la noticia
        if request.user == noticia.usuario or request.user.is_staff:
            messages.success(request, 'Noticia eliminada exitosamente.')
            return super().delete(request, *args, **kwargs)
        else:
            messages.error(request, 'No tienes permisos para eliminar esta noticia.')
            return HttpResponseRedirect(self.get_success_url())

def Detalle_noticia(request, pk):
    ctx = {}
    noticia = get_object_or_404(Noticia, pk=pk)

    # Incrementar el contador de visitas
    noticia.visitas += 1
    noticia.save()

    ctx['likes'] = noticia.count_likes()
    ctx['noticia'] = noticia
    ctx['checklike'] = request.user in noticia.likes.all()
    com = Comentario.objects.filter(noticia = noticia)
    ctx['comentarios'] = com
    return render(request, 'noticias/detalle_noticia.html', ctx)


def megusta(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.user in noticia.likes.all():
        noticia.likes.remove(request.user)
    else:
        noticia.likes.add(request.user.id)
    return redirect('/noticias/Detalle/'+str(noticia.id))


