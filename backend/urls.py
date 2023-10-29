from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from hoteles.controlador.UsuariosPOST import registrar_usuario, ver_usuariosGET, loginPOST
from hoteles.controlador.InmueblesPOST import crear_inmueble



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html')),  # Ruta vacía para cargar el formulario HTML en la URL raíz
    path('login/', loginPOST, name='login'),  # Ruta para procesar el formulario
    path("signup/", registrar_usuario, name="signup"),
    path("verUsuarios/", ver_usuariosGET, name="ver_usuariosGET"),
    path("crearInmueble/", crear_inmueble, name="crear_inmueble"),
]
