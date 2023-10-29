from django.http import JsonResponse
from hoteles.modelo.usuarios import Usuarios
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
import json


@csrf_exempt
def loginPOST(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Lee y carga los datos JSON del cuerpo de la solicitud

            email = data.get('email')
            password = data.get('password')

            if email and password:
                # Intenta autenticar al usuario con las credenciales proporcionadas
                user = authenticate(request, username=email, password=password)

                if user is not None:
                    # Autenticación exitosa
                    login(request, user)
                    return JsonResponse({'message': 'Usuario autenticado con éxito'})
                else:
                    return JsonResponse({'error': 'Credenciales de inicio de sesión inválidas'}, status=400)
            else:
                return JsonResponse({'error': 'Campos de email y contraseña requeridos'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Error en el formato de datos JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt
def registrar_usuario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Obtener datos del cuerpo de la solicitud

            email = data.get('email')
            password = data.get('password')
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            edad = data.get('edad')

            # Imprimir los datos para verificar que se reciben correctamente
            print("Datos recibos:", data)

            # Verificar si los campos requeridos no son nulos
            if email and password and nombre and apellido and edad:
                # Proceder con la creación y guardado del usuario
                usuario = Usuarios(
                    email=email,
                    password=password,
                    nombre=nombre,
                    apellido=apellido,
                    edad=edad
                )
                usuario.save()

                # Devolver una respuesta de éxito en formato JSON
                return JsonResponse({'message': 'Usuario registrado exitosamente'})
            else:
                # Manejar la situación donde los campos requeridos son nulos
                return JsonResponse({'error': 'Campos de usuario requeridos, algunos campos están vacíos'}, status=400)

        except json.JSONDecodeError:
            # Capturar errores al decodificar datos JSON
            return JsonResponse({'error': 'Error al procesar los datos JSON'}, status=400)
    else:
        # Manejar el caso en el que no se realice una solicitud POST
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
    

def ver_usuariosGET(request):
    if request.method == 'GET':
        # Recuperar todos los usuarios desde la base de datos utilizando el ORM de Django
        usuarios = Usuarios.objects.all()
        usuarios_data = [{'id': usuario.idUsuario, 'nombre': usuario.nombre, 'apellido': usuario.apellido, 'email': usuario.email, 'edad': usuario.edad} for usuario in usuarios]
        return JsonResponse({'usuarios': usuarios_data})
    else:
        # Manejar el caso en el que no se realice una solicitud GET
        # Puedes devolver un error o realizar otra acción aquí
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
@csrf_exempt
def ver_usuariosPOST(request):
    if request.method == 'POST':
        # Recuperaremos todos los usuarios y los devolveremos en formato JSON
        usuarios = Usuarios.objects.all()
        usuarios_data = [{'id': usuario.idUsuario, 'nombre': usuario.nombre, 'apellido': usuario.apellido, 'email': usuario.email, 'edad': usuario.edad} for usuario in usuarios]
        return JsonResponse({'usuarios': usuarios_data})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)





