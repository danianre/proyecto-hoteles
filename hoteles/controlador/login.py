from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from hoteles.modelo.usuarios import UsuarioManager
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        # Validación de campos requeridos
        if 'email' in request.POST and 'password' in request.POST:
            email = request.POST['email']
            password = request.POST['password']
            print(f"Email: {email}, Password: {password}")  # Agregar esta línea para imprimir los datos
        else:
            return JsonResponse({'error': 'Campos de email y contraseña requeridos'}, status=400)

        # Se utiliza método para autenticar al usuario
        user = UsuarioManager.autenticar_usuario(email, password)

        if user is not None:
            # Autenticación exitosa
            user_auth = authenticate(request, email=email, password=password)
            if user_auth is not None:
                login(request, user)
                return JsonResponse({'message': 'Usuario autenticado con éxito'})
            else:
                return JsonResponse({'error': 'Error en la autenticación de Django'}, status=400)
        else:
            return JsonResponse({'error': 'Error en la autenticación de la aplicación'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

# def principal_view(request):
#     # Vista para la página principal de usuarios
#     return render(request, 'principal')

