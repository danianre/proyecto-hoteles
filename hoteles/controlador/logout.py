from django.shortcuts import redirect
from django.contrib.auth import logout

def cerrar_sesion(request):
    logout(request)
    # Redirige a la página de inicio de sesión u otra página que desees después de cerrar sesión
    return redirect('login')