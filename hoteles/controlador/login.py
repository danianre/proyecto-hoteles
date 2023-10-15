from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from hoteles.modelo import usuarios

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Se utiliza método para autenticar al usuario
        user = usuarios.UsuarioManager.autenticar_usuario(email, password)
        
        if user is not None:
            # Si el usuario se autentica correctamente, inicia sesión y redirige a la página principal
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('principal') 
        else:
            # Si la autenticación falla, muestra un mensaje de error o vuelve a mostrar la vista de inicio de sesión
            return render(request, 'login', {'error_message': 'Email o contraseña incorrectos'})
    else:
        return render(request, 'login')  # Muestra la vista de inicio de sesión

def principal_view(request):
    # Vista para la página principal de usuarios
    return render(request, 'principal')

