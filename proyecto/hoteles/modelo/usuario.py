from django.db import models
from django.contrib.auth.hashers import make_password


class Usuario(models.Model):
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