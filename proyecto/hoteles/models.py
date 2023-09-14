from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#Formato tabla
class Tabla(models.Model):
    user = models.ForeingKey(UserTabla, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    producto = models.ManyToManyField(ProductoTabla) #muchos a muchos
    cantidad = models.IntegerField()


    class Meta:
        ordering = ['nombre']

    def get_productos(self):
        return "\n".join([p.nombre for p in self.producto.all()])

    def __str__(self):
        return self.nombre