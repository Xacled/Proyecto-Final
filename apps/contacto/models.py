from django.db import models


# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    RAZON_CHOICES = [
        ("problemas_tecnicos", "Problemas técnicos"),
        ("sugerencias", "Sugerencias"),
        ("publicidad", "Publicidad"),
        ("reportar", "Reportar Usuario/Post"),
    ]
    razon = models.CharField(
        max_length=20,
        choices=RAZON_CHOICES,
        default="problemas_tecnicos",
    )
    contenido = models.TextField()

    def __str__(self):
        return self.nombre
