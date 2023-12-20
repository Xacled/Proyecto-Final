from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Noticia, Categoria
from .forms import Formulario_Noticia, Formulario_Modificar_Noticia
from apps.comentarios.models import Comentario


def Home_Noticias(request):
    contexto = {}

    # Obtener todas las categorías para el menú de navegación
    contexto['categorias'] = Categoria.objects.all()

    # Filtrar noticias según la categoría, orden y búsqueda
    filtro = request.GET.get('categoria', '0')
    orden = request.GET.get('orden', '-creado')
    busqueda = request.GET.get('q', '')

    # Filtrar por categoría
    if filtro and filtro != '0':
        categoria_seleccionada = Categoria.objects.get(pk=filtro)
        todas = Noticia.objects.filter(categoria=categoria_seleccionada)
    else:
        todas = Noticia.objects.all()

    # Aplicar la búsqueda en título y contenido
    if busqueda:
        todas = todas.filter(titulo__icontains=busqueda) | todas.filter(contenido__icontains=busqueda)

    # Ordenar las noticias
    todas = todas.order_by(orden)

    # Implementar paginación
    paginator = Paginator(todas, 5)
    page = request.GET.get('page')

    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        noticias = paginator.page(1)
    except EmptyPage:
        noticias = paginator.page(paginator.num_pages)

    # Añadir noticias populares al contexto
    contexto['noticias_populares'] = Noticia.objects.order_by('-visitas')[:3]

    # Añadir noticias a contexto
    contexto['noticias'] = noticias

    return render(request, 'noticias/home_noticias.html', contexto)

   


class Cargar_noticia(LoginRequiredMixin, CreateView):
    model = Noticia
    template_name = 'noticias/cargar_noticia.html'
    form_class = Formulario_Noticia
    success_url = reverse_lazy('noticias:home_noticias')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class Modificar_noticia(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Noticia
    template_name = 'noticias/modificar_noticia.html'
    form_class = Formulario_Modificar_Noticia
    success_url = reverse_lazy('noticias:home_noticias')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def test_func(self):
        noticia = self.get_object()
        return self.request.user == noticia.usuario or self.request.user.is_colab

    def handle_no_permission(self):
        noticia = self.get_object()
        return redirect('noticias:detalle_noticia', pk=noticia.pk)


class Borrar_noticia(DeleteView):
    model = Noticia

    def get_success_url(self):
        return reverse_lazy('noticias:home_noticias')

    def delete(self, request, *args, **kwargs):
        noticia = self.get_object()

        if request.user == noticia.usuario or request.user.is_colab:
            messages.success(request, 'Noticia eliminada exitosamente.')
            return super().delete(request, *args, **kwargs)
        else:
            messages.error(request, 'No tienes permisos para eliminar esta noticia.')
            return HttpResponseRedirect(self.get_success_url())


def Detalle_noticia(request, pk):
    ctx = {}
    noticia = get_object_or_404(Noticia, pk=pk)

    noticia.visitas += 1
    noticia.save()

    ctx['likes'] = noticia.count_likes()
    ctx['noticia'] = noticia
    ctx['checklike'] = request.user in noticia.likes.all()
    com = Comentario.objects.filter(noticia=noticia)
    ctx['comentarios'] = com
    return render(request, 'noticias/detalle_noticia.html', ctx)


def megusta(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.user in noticia.likes.all():
        noticia.likes.remove(request.user)
    else:
        noticia.likes.add(request.user.id)
    return redirect('/noticias/Detalle/' + str(noticia.id))
