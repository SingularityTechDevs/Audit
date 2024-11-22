from django.contrib.auth.models import User
from django.db import models

class Usuario(User):
	def foto_usuario(self, filename):
		return f'Usuarios/{self.id}'
	# Agregar campo de imagen
	foto = models.ImageField(upload_to=foto_usuario, null=True, blank=True)


class Perfil(models.Model):
	def foto_usuario(self, filename):
		return f'Usuarios/{self.id}'
	# Agregar campo de imagen
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	foto = models.ImageField(upload_to=foto_usuario, null=True, blank=True)