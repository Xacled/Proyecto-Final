from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to="usuarios/", default="usuarios/default.png")
    bio = models.CharField(max_length=150, blank=True)
    is_colab = models.BooleanField(default=False)

    def __str__(self):
        return self.username
