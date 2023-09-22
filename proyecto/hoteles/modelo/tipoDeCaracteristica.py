from django.db import models


class TipoDeCaracteristica(models.Model):
    idtipoDeCaracteristicas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)