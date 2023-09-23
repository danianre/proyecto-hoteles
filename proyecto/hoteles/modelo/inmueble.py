from django.db import models
from proyecto.hoteles.modelo.caracteristica import Caracteristica
from proyecto.hoteles.modelo.ciudad import Ciudad
from proyecto.hoteles.modelo.sector import Sector
from proyecto.hoteles.modelo.direccion import Direccion


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
    caracteristicas = models.ManyToManyField(Caracteristica)

    def __str__(self):
        return self.nombre
    

class InmuebleDAO(models.Model):
    @classmethod
    def ver_inmuebles(cls):
        # Recuperar todos los inmuebles desde la base de datos
        inmuebles = Inmueble.objects.all()
        return inmuebles

    @classmethod
    def filtrar_por_ubicacion_y_tipo(cls, ubicacion, tipo_inmueble):
        # Filtra los inmuebles por ubicación y tipo de inmueble
        inmuebles = cls.objects.filter(ubicacion=ubicacion, tipo_inmueble=tipo_inmueble)
        return inmuebles
    
    @classmethod
    def filtrar_por_rango_de_precio(cls, precio_min, precio_max):
        # Filtra los inmuebles por un rango de precios (precio_min <= precio <= precio_max)
        inmuebles = cls.objects.filter(precio__gte=precio_min, precio__lte=precio_max)
        return inmuebles
    
    @classmethod
    def filtrar_por_antiguedad(cls, antiguedad):
        # Filtra los inmuebles por antiguedad
        inmuebles = cls.objects.filter(antiguedad=antiguedad)
        return inmuebles
    
    @classmethod
    def filtrar_por_caracteristicas(cls, caracteristicas):
        # Filtra los inmuebles que tienen todas las características especificadas
        inmuebles = cls.objects.filter(caracteristicas__in=caracteristicas).distinct()
        return inmuebles