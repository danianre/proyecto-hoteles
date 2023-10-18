from django.contrib import admin
from hoteles.modelo.usuarios import Usuarios
from hoteles.modelo.inmuebles import Inmuebles
from hoteles.modelo.caracteristicas import Caracteristicas
from hoteles.modelo.ciudades import Ciudades
from hoteles.modelo.departamentos import Departamentos
from hoteles.modelo.inmueblesPorUsuarios import InmueblesPorUsuarios
from hoteles.modelo.paises import Paises
from hoteles.modelo.sectores import Sectores
from hoteles.modelo.tiposDeCaracteristicas import TiposDeCaracteristicas

# Register your models here. Crud

admin.site.register(Usuarios)
admin.site.register(Inmuebles)
admin.site.register(Caracteristicas)
admin.site.register(Ciudades)
admin.site.register(Departamentos)
admin.site.register(InmueblesPorUsuarios)
admin.site.register(Paises)
admin.site.register(Sectores)
admin.site.register(TiposDeCaracteristicas)


