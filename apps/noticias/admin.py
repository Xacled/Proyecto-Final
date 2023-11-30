from django.contrib import admin

from .models import Noticia, Categoria


admin.site.register(Noticia)
admin.site.register(Categoria)