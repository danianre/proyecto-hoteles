from django.db import models

class Paises(models.Model):
    idPais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
