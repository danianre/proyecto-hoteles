from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from hoteles.controlador.UsuariosPOST import registrar_usuario, ver_usuariosGET, autenticar_usuario
from hoteles.controlador.login import login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="base.html")),
    path("signup/", registrar_usuario, name="registrar_usuario"),
    path("verUsuarios/", ver_usuariosGET, name="ver_usuariosGET"),
    path("login/", login_view, name="login_view"),
]
