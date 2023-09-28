from django.db import models

from modelo.paises import Paises

class Departamentos(models.Model):
    idDepartamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    idPais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
