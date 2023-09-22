from django.db import models
from tipoDeCaracteristica import TipoDeCaracteristica

class Caracteristica(models.Model):
    idCaracteristicas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    idTipoCaracteristica = models.ForeignKey(TipoDeCaracteristica, on_delete=models.CASCADE)