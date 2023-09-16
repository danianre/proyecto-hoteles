from django.db import models

# Create your models here.


class Ciudad(models.Model):
    def __str__(self):
        return 

class Direccion(models.Model):
    def __str__(self):
        return 

class Sector(models.Model):
    def __str__(self):
        return 
    
class Inmueble(models.Model):
    idInmueble = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    estrato = models.IntegerField()
    cantidadDeHabitantes = models.IntegerField()
    cantidadDeBaños = models.IntegerField()
    cantidadDeParqueaderos = models.IntegerField()
    piso = models.IntegerField()
    antiguedad = models.IntegerField()
    estado = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    areaPrivada = models.IntegerField()
    areaConstruida = models.IntegerField()
    precioAdministracion = models.IntegerField()
    precio = models.IntegerField()
    idSector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    idDireccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    idCiudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    