from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usuario(AbstractUser):
    def foto_usuario(self, filename):
        return f'Usuarios/{self.id}'

    foto = models.ImageField(upload_to=foto_usuario, blank=True)
     
    def __str__(self):
        return f"{self.username}-{self.first_name}  {self.last_name}"