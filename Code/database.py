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

    def insert_medicion(self, pulso_cardiaco, oxigenacion):
        """Función para insertar una medición en la base de datos."""
        if not self.connection:
            print("Conexión no establecida. Llame primero a connect().")
            return

        try:
            cursor = self.connection.cursor()
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Insertar una nueva medición
            query = "INSERT INTO mediciones (fecha_hora, pulso_cardiaco, oxigenacion) VALUES (%s, %s, %s)"
            cursor.execute(query, (now, pulso_cardiaco, oxigenacion))

            # Confirmar la inserción
            self.connection.commit()

            print("Medición insertada exitosamente.")
        except MySQLdb.Error as e:
            print("Error al insertar los datos: ", e)
        finally:
            # Cerrar cursor
            if cursor:
                cursor.close()

# Ejemplo de uso
db_manager = DatabaseManager(user='tu_usuario', passwd='tu_contraseña', db='monitoring')
db_manager.connect()
db_manager.insert_medicion(80, 95)
db_manager.close()
