import MySQLdb
import datetime

def insert_medicion(pulso_cardiaco, oxigenacion):
    """Función para insertar una medición en la base de datos."""
    try:
        # Conexión a la base de datos
        connection = MySQLdb.connect(
            host='localhost',
            user='root',  # Usa tu usuario correcto
            passwd='root',  # Reemplaza con tu contraseña real
            db='monitoring'
        )

        cursor = connection.cursor()
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Insertar una nueva medición
        query = "INSERT INTO mediciones (fecha_hora, pulso_cardiaco, oxigenacion) VALUES (%s, %s, %s)"
        cursor.execute(query, (now, pulso_cardiaco, oxigenacion))
        
        # Confirmar la inserción
        connection.commit()
        
        print("Medición insertada exitosamente.")
    except MySQLdb.Error as e:
        print("Error al insertar los datos: ", e)
    finally:
        # Cerrar la conexión
        if connection:
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")


