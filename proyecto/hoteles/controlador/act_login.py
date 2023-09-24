from django.shortcuts import render, redirect
from proyecto.hoteles.controlador.mdb.mdbUsuario import autenticar_usuario 

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Intenta autenticar al usuario
        user = autenticar_usuario(email, password)
        
        if user is not None:
            # Si el usuario se autentica correctamente, guarda sus datos en la sesión
            request.session['ID_USUARIO'] = user.idUsuario
            request.session['EMAIL_USUARIO'] = user.email
            request.session['NOMBRE_USUARIO'] = user.nombre
            request.session['APELLIDO_USUARIO'] = user.apellido
            request.session['EDAD_USUARIO'] = user.edad
        else:
            # Si el usuario no existe, muestra un mensaje de error o vuelve a mostrar el formulario de inicio de sesión
            # Puedes manejar esto en la plantilla
            return render(request, 'login.html', {'error_message': 'email o contraseña incorrectos'})
    else:
        return render(request, 'login.html')  # Muestra el formulario de inicio de sesión

def principal_view(request):
    # Vista para la página principal de administradores
    # Aquí puedes agregar lógica específica para administradores
    return render(request, 'principal.html')

def principal_user_view(request):
    # Vista para la página principal de usuarios normales
    # Aquí puedes agregar lógica específica para usuarios normales
    return render(request, 'principal_user.html')
