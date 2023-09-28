from django.db import models

class Sectores(models.Model):
    idSector = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre