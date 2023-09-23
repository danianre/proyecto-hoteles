from django.db import models
from proyecto.hoteles.modelo.usuario import Usuario
from proyecto.hoteles.modelo.inmueble import Inmueble


class inmueblePorUsuario(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idInmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    clasificacion = models.FloatField()