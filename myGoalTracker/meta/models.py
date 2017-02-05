from django.db import models
from usuario.models import Usuario

from datetime import datetime


class MetaAbstracta(models.Model):
    abstract = True
    titulo = models.CharField(max_length=80, default='Título')
    descripcion = models.CharField(max_length=200, default='Descripción')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_comienzo = models.DateTimeField(null=True, blank=True, default=datetime.now)


class Meta(MetaAbstracta):
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, blank=True, null=True)
