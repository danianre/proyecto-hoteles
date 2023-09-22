from django.db import models


class Dirección(models.Model):
    idDirección = models.AutoField(primary_key=True)
    sufijo = models.CharField(max_length=100)
    numero = models.IntegerField()
    numeroDeVia = models.IntegerField()
    numeroDeLaCasa = models.IntegerField()
    codigoPostal = models.IntegerField()
    idTipoDeVia = models.IntegerField()
    
    def __str__(self):
        return 
