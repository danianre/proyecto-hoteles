from django.db import models

class Sector(models.Model):
    idSector = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return 