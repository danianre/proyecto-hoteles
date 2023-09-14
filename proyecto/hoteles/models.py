from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#Formato tabla ejemplo
class Tabla(models.Model):
    nombre = models.CharField(max_length=50)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre
