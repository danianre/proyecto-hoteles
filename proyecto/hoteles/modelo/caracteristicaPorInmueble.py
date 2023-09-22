from django.db import models
from caracteristica import Caracteristica
from inmueble import Inmueble

class CaracteristicasPorInmueble(models.Model):
    idCaracteristica = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
    idInmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)