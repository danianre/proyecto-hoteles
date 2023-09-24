from django.db import models
from django.contrib.auth.hashers import make_password
from proyecto.hoteles.modelo import DataSource


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

class UsuarioDAO(models.Model):
    @classmethod
    def autenticar_usuario(cls, email, password):
        # Se crea la instancia de DataSource para hacer la conexión
        data_source = DataSource()

        # Se llama al método ejecutarConsulta para devolver el usuario
        # que cumple con el email y contraseña recibidos del login
        data_table = data_source.ejecutar_consulta(
            "SELECT * FROM usuario WHERE email = %s AND password = %s",
            (email, password)
        )

        usuario = None

        # Si data_table contiene una fila, significa que se encontró el usuario en la base de datos
        if len(data_table) == 1:
            usuario_data = data_table[0]
            usuario = cls(
                idUsuario=usuario_data["idUsuario"],
                email=usuario_data["email"],
                password=usuario_data["password"],
                nombre=usuario_data["nombre"],
                apellido=usuario_data["apellido"],
                edad=usuario_data["edad"],
            )

        return usuario
    
    @classmethod
    def registrar_usuario(cls, usuario):
        data_source = DataSource()

        stmt = """
            INSERT INTO usuario (nombre, apellido, email, password, edad)
            VALUES (%s, %s, %s, %s, %s)
        """

        resultado = data_source.ejecutar_actualizacion(
            stmt,
            (
                usuario.email,
                usuario.password,
                usuario.nombre,
                usuario.apellido,  
                usuario.edad,
            ),
        )

        return resultado
    
    @classmethod
    def ver_usuarios(cls):
        data_source = DataSource()

        data_table = data_source.ejecutar_consulta("SELECT * FROM usuario")

        usuarios = []

        for usuario_data in data_table:
            usuario = cls(
                idUsuario=usuario_data["idUsuario"],
                email=usuario_data["email"],
                password=usuario_data["password"],
                nombre=usuario_data["nombre"],
                apellido=usuario_data["apellido"],
                idGenero=usuario_data["idGenero"],
            )
            usuarios.append(usuario)

        return usuarios