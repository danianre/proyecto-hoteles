from django.db import models
from hoteles.modelo.paises import Paises
from hoteles.modelo.departamentos import Departamentos
from hoteles.modelo.caracteristicas import Caracteristicas
from hoteles.modelo.ciudades import Ciudades
from hoteles.modelo.sectores import Sectores


class Inmuebles(models.Model):
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
    idCiudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    idDepartamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    idPais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    idSector = models.ForeignKey(Sectores, on_delete=models.CASCADE)
    # caracteristica = models.ManyToManyField(Caracteristicas)

    def __str__(self):
        return self.nombre
    

    def ver_inmuebles(cls):
        # Recuperar todos los inmuebles desde la base de datos
        inmuebles = Inmuebles.objects.all()
        return inmuebles

    def filtrar_por_caracteristicas(cls, caracteristicas):
        # Filtra los inmuebles que tienen todas las características especificadas
        inmuebles = cls.objects.filter(caracteristicas__in=caracteristicas).distinct()
        return inmuebles
    
    
    def crear_inmueble(cls, nombre, descripcion, estrato, cantidadDeHabitantes, cantidadDeBaños, cantidadDeParqueaderos, piso, antiguedad, estado, url, areaPrivada, areaConstruida, precioAdministracion, precio, direccion, idSector, idCiudad, idDepartamento, idPais, caracteristicas):
        inmueble = cls(
            nombre=nombre,
            descripcion=descripcion,
            estrato=estrato,
            cantidadDeHabitantes=cantidadDeHabitantes,
            cantidadDeBaños=cantidadDeBaños,
            cantidadDeParqueaderos=cantidadDeParqueaderos,
            piso=piso,
            antiguedad=antiguedad,
            estado=estado,
            url=url,
            areaPrivada=areaPrivada,
            areaConstruida=areaConstruida,
            precioAdministracion=precioAdministracion,
            precio=precio,
            direccion=direccion,
            idSector=idSector,
            idCiudad=idCiudad,
            idDepartamento=idDepartamento,
            idPais=idPais,
        )
        inmueble.save()
        # inmueble.caracteristica.set(caracteristica)
        return inmueble