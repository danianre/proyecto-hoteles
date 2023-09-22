from django.db import models
from usuario import Usuario
from inmueble import Inmueble


class inmueblePorUsuario(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idInmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    clasificacion = models.FloatField()