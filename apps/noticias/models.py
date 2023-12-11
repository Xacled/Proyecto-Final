from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):

    creado = models.DateTimeField(
        'creado',
        auto_now_add=True
    )
    modificado = models.DateTimeField(
        'modificado',
        auto_now=True
    )
    titulo = models.CharField(max_length=250)
    contenido = models.TextField()
    # para usar ImegeField, necesito tener instalado la libreria pillow
    # pip install pillow
    imagen = models.ImageField(upload_to='noticias')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    visitas = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name="not_megustas",blank=True)

    def count_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.titulo
