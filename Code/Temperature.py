import adafruit_dht
import board
import time

# Inicializa el sensor DHT11.
# Reemplaza 'D4' con el pin al que está conectado tu sensor DHT11.
# Por ejemplo, para GPIO4 en Raspberry Pi, usarías board.D4.
sensor = adafruit_dht.DHT11(board.D4)

while True:
    try:
        # Lee la humedad y la temperatura del sensor.
        temperature = sensor.temperature
        humidity = sensor.humidity
        
        # Imprime los valores leídos.
        print(f"Temperatura: {temperature}°C  Humedad: {humidity}%")

    except RuntimeError as error:
        # Errores que suelen suceder de forma rutinaria, como lecturas fallidas debido a temporización.
        print(error.args[0])
        
    except Exception as error:
        sensor.exit()
        raise error

    # Espera un poco antes de leer nuevamente
    time.sleep(2.0)