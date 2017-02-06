from django.db import models
from django.contrib.auth.models import User

from PIL import Image


class Usuario(models.Model):
    """  Este modelo one-to-one es frecuentemente llamado modelo Perfil """

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # pip install Pillow
    foto = models.ImageField(upload_to = 'imagenes/', default = 'imagenes/None/no-img.jpg')
