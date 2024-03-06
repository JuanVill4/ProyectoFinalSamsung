import MySQLdb
import datetime

class MonitoreoDB:
    def __init__(self, host='localhost', user='root', passwd='root', db='monitoring'):
        """Inicializa la conexión a la base de datos."""
        self.connection = None
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

    def connect(self):
        """Establece la conexión a la base de datos."""
        try:
            self.connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                db=self.db
            )
            print("Conexión a MySQL establecida exitosamente.")
        except MySQLdb.Error as e:
            print("Error al conectar a MySQL: ", e)

    def close(self):
        """Cierra la conexión a la base de datos."""
        if self.connection:
            self.connection.close()
            print("Conexión a MySQL cerrada")

    # def insert_medicion(self, pulso_cardiaco, oxigenacion):
    #     """Función para insertar una medición en la base de datos."""
    #     if not self.connection:
    #         print("Conexión no establecida. Llame primero a connect().")
    #         return

    #     try:
    #         cursor = self.connection.cursor()
    #         now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #         # Insertar una nueva medición
    #         query = "INSERT INTO mediciones (fecha_hora, pulso_cardiaco, oxigenacion) VALUES (%s, %s, %s)"
    #         #query = "INSERT INTO sensor_distancia (distancia) VALUES (%s)"
    #         cursor.execute(query, (now, pulso_cardiaco, oxigenacion))
    #         #cursor.execute(query, (now, distancia))

    #         # Confirmar la inserción
    #         self.connection.commit()

    #         print("Medición insertada exitosamente.")
    #     except MySQLdb.Error as e:
    #         print("Error al insertar los datos: ", e)
    #     finally:
    #         # Cerrar cursor
    #         if cursor:
    #             cursor.close()
    def insert_medicion(self, **kwargs):
        if not self.connection:
            print("Conexión no establecida. Llame primero a connect().")
            return

        try:
            cursor = self.connection.cursor()
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if 'distancia' in kwargs:
                # Insertar solo distancia en la tabla sensor_distancia
                query = "INSERT INTO sensor_distancia (fecha_hora, distancia) VALUES (%s, %s)"
                cursor.execute(query, (now, kwargs['distancia']))
            else:
                # Insertar pulso cardiaco y oxigenación en la tabla mediciones
                query = "INSERT INTO mediciones (fecha_hora, pulso_cardiaco, oxigenacion) VALUES (%s, %s, %s)"
                cursor.execute(query, (now, kwargs.get('pulso_cardiaco', None), kwargs.get('oxigenacion', None)))

            # Confirmar la inserción
            self.connection.commit()

            print("Medición insertada exitosamente.")
        except Exception as e:
            print("Error al insertar los datos: ", e)
        finally:
            # Cerrar cursor
            if cursor:
                cursor.close()


