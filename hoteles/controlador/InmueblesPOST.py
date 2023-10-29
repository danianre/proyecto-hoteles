from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from hoteles.modelo.inmuebles import Inmuebles, Sectores, Ciudades, Departamentos, Paises
import json

@csrf_exempt
def crear_inmueble(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Obtener datos del cuerpo de la solicitud

            # Verificar que se tienen los datos requeridos
            required_fields = ['nombre', 'descripcion', 'estrato', 'cantidadDeHabitantes', 'cantidadDeBaños', 
                               'cantidadDeParqueaderos', 'piso', 'antiguedad', 'estado', 'url', 'areaPrivada', 
                               'areaConstruida', 'precioAdministracion', 'precio', 'direccion', 
                               'idSector', 'idCiudad', 'idDepartamento', 'idPais']

            if not all(field in data for field in required_fields):
                return JsonResponse({'error': 'Faltan campos requeridos'}, status=400)

            # Obtener datos de la solicitud
            nombre = data['nombre']
            descripcion = data['descripcion']
            estrato = data['estrato']
            cantidad_habitantes = data['cantidadDeHabitantes']
            cantidad_baños = data['cantidadDeBaños']
            cantidad_parqueaderos = data['cantidadDeParqueaderos']
            piso = data['piso']
            antiguedad = data['antiguedad']
            estado = data['estado']
            url = data['url']
            area_privada = data['areaPrivada']
            area_construida = data['areaConstruida']
            precio_administracion = data['precioAdministracion']
            precio = data['precio']
            direccion = data['direccion']
            id_sector = data['idSector']
            id_ciudad = data['idCiudad']
            id_departamento = data['idDepartamento']
            id_pais = data['idPais']

            # Buscar los objetos relacionados
            sector = Sectores.objects.get(pk=id_sector)
            ciudad = Ciudades.objects.get(pk=id_ciudad)
            departamento = Departamentos.objects.get(pk=id_departamento)
            pais = Paises.objects.get(pk=id_pais)

            # Crear el inmueble en la base de datos
            inmueble = Inmuebles(
                nombre=nombre,
                descripcion=descripcion,
                estrato=estrato,
                cantidadDeHabitantes=cantidad_habitantes,
                cantidadDeBaños=cantidad_baños,
                cantidadDeParqueaderos=cantidad_parqueaderos,
                piso=piso,
                antiguedad=antiguedad,
                estado=estado,
                url=url,
                areaPrivada=area_privada,
                areaConstruida=area_construida,
                precioAdministracion=precio_administracion,
                precio=precio,
                idCiudad=ciudad,
                idDepartamento=departamento,
                direccion=direccion,
                idPais=pais,
                idSector=sector
            )
            inmueble.save()

            # Retorna una respuesta JSON con la confirmación de creación
            return JsonResponse({'message': 'Inmueble creado con éxito'})

        except json.JSONDecodeError:
            # Capturar errores al decodificar datos JSON
            return JsonResponse({'error': 'Error al procesar los datos JSON'}, status=400)
        except (Sectores.DoesNotExist, Ciudades.DoesNotExist, Departamentos.DoesNotExist, Paises.DoesNotExist):
            # Capturar errores si no se encuentran los objetos relacionados
            return JsonResponse({'error': 'Objeto relacionado no encontrado'}, status=400)
        except Exception as e:
            # Capturar cualquier otra excepción
            return JsonResponse({'error': f'Error al crear el inmueble: {str(e)}'}, status=400)
    else:
        # Manejar el caso en el que no se realice una solicitud POST
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def ver_inmueblesPOST(request):
    if request.method == 'POST':
        # Aquí maneja la lógica del controlador para el método POST
        # Recuperar todos los inmuebles desde la base de datos
        inmuebles = Inmuebles.objects.all()
        # Realizar cualquier procesamiento adicional necesario
        # Devolver una respuesta JSON o HTML, según corresponda
        # Por ejemplo, aquí devolveré una respuesta JSON
        inmuebles_data = [inmueble.to_dict() for inmueble in inmuebles]
        return JsonResponse({'inmuebles': inmuebles_data})
    else:
        # Manejar el caso en el que no se realice una solicitud POST
        # Puedes devolver un error o realizar otra acción aquí
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def ver_inmueblesGET(request):
    if request.method == 'GET':
        inmuebles = Inmuebles.objects.all()
        inmuebles_data = [inmueble.to_dict() for inmueble in inmuebles]
        return JsonResponse({'inmuebles': inmuebles_data})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def filtrar_inmuebles_por_precio(request):
    if request.method == 'POST':
        # Recuperar los valores de precio mínimo y precio máximo del cuerpo de la solicitud POST
        precio_min = request.POST.get('precio_min')
        precio_max = request.POST.get('precio_max')

        # Validar que los valores sean numéricos
        if not precio_min.isdigit() or not precio_max.isdigit():
            return JsonResponse({'error': 'Los valores de precio deben ser numéricos'}, status=400)

        # Convertir los valores a números enteros
        precio_min = int(precio_min)
        precio_max = int(precio_max)

        # Filtrar los inmuebles por un rango de precios (precio_min <= precio <= precio_max)
        inmuebles = Inmuebles.objects.filter(precio__gte=precio_min, precio__lte=precio_max)

        # Realizar cualquier procesamiento adicional necesario
        # Devolver una respuesta JSON con los inmuebles encontrados
        inmuebles_data = [{'id': inmueble.idInmueble, 'precio': inmueble.precio} for inmueble in inmuebles]

        return JsonResponse({'inmuebles': inmuebles_data})
    else:
        # Manejar el caso en el que no se realice una solicitud POST
        # Puedes devolver un error o realizar otra acción aquí
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def filtrar_inmuebles_por_antiguedad(request):
    if request.method == 'POST':
        # Recuperar el valor de antigüedad del cuerpo de la solicitud POST
        antiguedad = request.POST.get('antiguedad')

        # Validar que el valor sea un número entero
        if not antiguedad.isdigit():
            return JsonResponse({'error': 'La antigüedad debe ser un número entero'}, status=400)

        # Convertir el valor a un número entero
        antiguedad = int(antiguedad)

        # Filtrar los inmuebles por antigüedad
        inmuebles = Inmuebles.objects.filter(antiguedad=antiguedad)

        # Realizar cualquier procesamiento adicional necesario
        # Devolver una respuesta JSON con los inmuebles encontrados
        inmuebles_data = [{'id': inmueble.idInmueble, 'antiguedad': inmueble.antiguedad} for inmueble in inmuebles]

        return JsonResponse({'inmuebles': inmuebles_data})
    else:
        # Manejar el caso en el que no se realice una solicitud POST
        # Puedes devolver un error o realizar otra acción aquí
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def filtrar_inmuebles_por_caracteristicas(request):
    if request.method == 'POST':
        # Recuperar las características del cuerpo de la solicitud POST
        caracteristicas = request.POST.getlist('caracteristicas[]')

        # Validar que se proporcionen características
        if not caracteristicas:
            return JsonResponse({'error': 'Debes proporcionar al menos una característica'}, status=400)

        # Filtrar los inmuebles que tienen todas las características especificadas
        inmuebles = Inmuebles.objects.filter(caracteristicas__in=caracteristicas).distinct()

        # Realizar cualquier procesamiento adicional necesario
        # Devolver una respuesta JSON con los inmuebles encontrados
        inmuebles_data = [{'id': inmueble.idInmueble, 'caracteristicas': list(inmueble.caracteristicas.all())} for inmueble in inmuebles]

        return JsonResponse({'inmuebles': inmuebles_data})
    else:
        # Manejar el caso en el que no se realice una solicitud POST
        # Puedes devolver un error o realizar otra acción aquí
        return JsonResponse({'error': 'Método no permitido'}, status=405)
