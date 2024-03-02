import Adafruit_DHT
import time

# Inicializa el sensor DHT11.
# Reemplaza 'D4' con el pin al que está conectado tu sensor DHT11.
# Por ejemplo, para GPIO4 en Raspberry Pi, usarías board.D4.
sensor = Adafruit_DHT.DHT11
pin = '13'

while True:
    # Intenta obtener la lectura del sensor.
    # La función read_retry intenta obtener lecturas del sensor varias veces (hasta 15 por defecto)
    # para minimizar los errores de lectura.
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        # Imprime los resultados.
        print('Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temperature, humidity))
    else:
        # Si no se pudo obtener la lectura, imprime un mensaje de error.
        print('Fallo la lectura del sensor. Intente de nuevo!')
    
    # Espera 2 segundos antes de la próxima lectura.
    time.sleep(2)