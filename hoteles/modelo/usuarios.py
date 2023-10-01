from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model


class Usuarios(models.Model):
    idUsuario = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length = 30, unique = True)
    password = models.CharField(max_length = 255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.PositiveIntegerField()


    def save(self, **kwargs):
        clave = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, clave)
        super().save(**kwargs)

class UsuarioManager(models.Manager):
    @classmethod
    def autenticar_usuario(cls, email, password):
        try:
            # Buscar un usuario por correo y contraseña en la base de datos
            usuario = get_user_model().objects.get(email=email, password=password)
            return usuario
        except get_user_model().DoesNotExist:
            return None
    
    @classmethod
    def registrar_usuario(usuario_data):
        try:
            # Crea un nuevo objeto Usuario y guárdalo en la base de datos
            usuario = Usuarios(
                email=usuario_data['email'],
                password=usuario_data['password'],
                nombre=usuario_data['nombre'],
                apellido=usuario_data['apellido'],
                edad=usuario_data['edad'],
            )
            usuario.save()
            return usuario
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir al guardar el usuario
            # Por ejemplo, manejar la excepción de violación de restricción única en el campo 'email'
            return None
    
    @classmethod
    def ver_usuarios(cls):
        # Recuperar todos los usuarios desde la base de datos utilizando el ORM de Django
        usuarios = cls.get_queryset().all()
        return usuarios
    