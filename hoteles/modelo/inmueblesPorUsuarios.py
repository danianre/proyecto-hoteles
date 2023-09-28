from django.db import models
from modelo.usuarios import Usuarios
from modelo.inmuebles import Inmuebles


class inmueblePorUsuario(models.Model):
    idUsuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    idInmueble = models.ForeignKey(Inmuebles, on_delete=models.CASCADE)
    clasificacion = models.FloatField()