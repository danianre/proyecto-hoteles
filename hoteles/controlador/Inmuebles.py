from django.http import JsonResponse
from hoteles.modelo.inmuebles import Inmuebles

def ver_inmuebles(request):
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
