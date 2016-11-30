from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    usuario = models.OneToOneField(User)
    # pip install Pillow
    foto = models.ImageField(upload_to = 'imagenes/', default = 'imagenes/None/no-img.jpg')
