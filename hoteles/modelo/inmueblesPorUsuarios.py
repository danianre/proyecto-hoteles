from django.db import models
from hoteles.modelo.usuarios import Usuarios
from hoteles.modelo.inmuebles import Inmuebles


class inmueblesPorUsuarios(models.Model):
    idUsuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    idInmueble = models.ForeignKey(Inmuebles, on_delete=models.CASCADE)
    clasificacion = models.FloatField()