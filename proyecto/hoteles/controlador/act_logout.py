from django.shortcuts import redirect

def cerrar_sesion(request):
    # Cierra la sesión actual
    request.session.flush()
    
    # Redirecciona a la vista de login (reemplaza 'nombre_de_tu_ruta_login' con la ruta real)
    return redirect('nombre_de_tu_ruta_login')
