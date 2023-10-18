from django.http import JsonResponse
from hoteles.modelo.usuarios import Usuarios
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST


@require_POST
def autenticar_usuario(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Buscar un usuario por correo y contraseña en la base de datos
            Usuario = get_user_model()
            Usuario.objects.get(email=email, password=password)
            # Aquí se puede realizar cualquier acción adicional si el usuario se autentica exitosamente
            return JsonResponse({'message': 'Usuario autenticado exitosamente'})
        except Usuario.DoesNotExist:
            # Manejar el caso en el que el usuario no se encuentre en la base de datos o la autenticación sea incorrecta
            return JsonResponse({'error': 'Credenciales inválidas'}, status=401)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def registrar_usuario(request):
    if request.method == 'POST':
        try:
            # Recuperar los datos del usuario del cuerpo de la solicitud POST
            usuario_data = {
                'email': request.POST.get('email'),
                'password': request.POST.get('password'),
                'nombre': request.POST.get('nombre'),
                'apellido': request.POST.get('apellido'),
                'edad': request.POST.get('edad'),
            }

            # Crear un nuevo objeto Usuario y guardarlo en la base de datos
            usuario = Usuarios(
                email=usuario_data['email'],
                password=usuario_data['password'],
                nombre=usuario_data['nombre'],
                apellido=usuario_data['apellido'],
                edad=usuario_data['edad'],
            )
            usuario.save()

            # Devolver una respuesta de éxito en formato JSON
            return JsonResponse({'message': 'Usuario registrado exitosamente'})

        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir al guardar el usuario
            # Por ejemplo, manejar la excepción de violación de restricción única en el campo 'email'
            return JsonResponse({'error': 'Error al registrar el usuario'}, status=400)

    else:
        # Manejar el caso en el que no se realice una solicitud POST
        # Puedes devolver un error o realizar otra acción aquí
        return JsonResponse({'error': 'Método no permitido'}, status=405)

# def ver_usuariosGET(request):
#     if request.method == 'GET':
#         # Recuperar todos los usuarios desde la base de datos utilizando el ORM de Django
#         usuarios = Usuarios.objects.all()
#         usuarios_data = [{'id': usuario.idUsuario, 'nombre': usuario.nombre, 'apellido': usuario.apellido, 'email': usuario.email, 'edad': usuario.edad} for usuario in usuarios]
#         return JsonResponse({'usuarios': usuarios_data})
#     else:
#         # Manejar el caso en el que no se realice una solicitud GET
#         # Puedes devolver un error o realizar otra acción aquí
#         return JsonResponse({'error': 'Método no permitido'}, status=405)
    

def ver_usuariosPOST(request):
    if request.method == 'POST':
        # Recuperaremos todos los usuarios y los devolveremos en formato JSON
        usuarios = Usuarios.objects.all()
        usuarios_data = [{'id': usuario.idUsuario, 'nombre': usuario.nombre, 'apellido': usuario.apellido, 'email': usuario.email, 'edad': usuario.edad} for usuario in usuarios]
        return JsonResponse({'usuarios': usuarios_data})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)





