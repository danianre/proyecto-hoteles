from django.db import models
from modelo.tiposDeCaracteristicas import TiposDeCaracteristicas

class Caracteristicas(models.Model):
    idCaracteristicas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    idTipoCaracteristica = models.ForeignKey(TiposDeCaracteristicas, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre