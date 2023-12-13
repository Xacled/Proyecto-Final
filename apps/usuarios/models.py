from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    picture = models.ImageField(upload_to="usuarios/",default="usuarios/default.jpg")
    
    is_colab = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username