from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from hoteles.controlador.Usuarios import registrar_usuario


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="base.html")),
    path("signup/", registrar_usuario, name="registrar_usuario"),
]
