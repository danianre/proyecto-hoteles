from django.db import connection

class DataSource:
    def __init__(self):
        self.connection = connection

    def ejecutar_consulta(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            result = cursor.fetchall()
        return result

    def ejecutar_actualizacion(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            return cursor.rowcount
