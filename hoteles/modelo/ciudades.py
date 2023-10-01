from django.db import models
from hoteles.modelo.departamentos import Departamentos


class Ciudades(models.Model):
    idCiudad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    idDepartamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
