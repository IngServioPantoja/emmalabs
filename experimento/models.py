from django.db import models

from protocolo.models import Protocolo

class Experimento(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    protocolos = models.ManyToManyField(Protocolo)