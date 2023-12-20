from django.db import models
from django.conf import settings
from apps.noticias.models import Noticia

# Create your models here.


class Comentario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField("creado", auto_now_add=True)
    fecha_modificacion = models.DateTimeField("modificado", auto_now=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.noticia.titulo}"
