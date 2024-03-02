from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont
import sys
from pathlib import Path
import time
from gpiozero import LED, Button
from db import insert_medicion
# Agrega la carpeta Oxigen al sys.path
oxigen_path = Path(__file__).resolve().parent / 'Oxigen'
sys.path.append(str(oxigen_path))
from hrmonitor import HeartRateMonitor

# Inicialización del bus I2C y dirección del dispositivo OLED
serial = i2c(port=1, address=0x3C)

# Inicialización del dispositivo OLED con el controlador SH1106
device = sh1106(serial, rotate=0)
# Configuración de la fuente así como cálculo para posición centrada
font_path = "ProyectoFinalSamsungEquipo10/Code/templates/ALBA____.TTF"
font = ImageFont.truetype(font_path, 18)
with canvas(device) as draw:
        ancho_texto, alto_texto = draw.textsize("Pulsioximetro", font=font)
        ancho_display, alto_display = device.width, device.height
        x = (ancho_display - ancho_texto) / 2

        ancho_texto1, alto_texto1 = draw.textsize("Dedo no detectado")
        x1 = (ancho_display - ancho_texto1) / 2
# Configuración de LEDs y botones
led_verde = LED(23)  # Asume que el LED verde está conectado al pin GPIO 23
led_rojo = LED(18)  # Asume que el LED rojo está conectado al pin GPIO 18
boton = Button(12)  # Asume que el botón está conectado al pin GPIO 2

# Estado del sistema
sistema_encendido = False

# Función para encender y apagar el sistema
def toggle_sistema():
    global sistema_encendido
    sistema_encendido = not sistema_encendido
    if sistema_encendido:
        print("Sistema encendido")
        device.show()  # Reactiva la pantalla OLED

    else:
        print("Sistema apagado")
        device.hide()  # Apaga la pantalla OLED
        led_verde.off()  # Asegura que el LED verde se apague cuando el sistema se apague
        led_rojo.off()  # Enciende el LED rojo para indicar que el sistema está apagado

boton.when_pressed = toggle_sistema

# Función para mostrar los datos del sensor en el OLED
def display_sensor_data(hrm):
    if sistema_encendido:
        with canvas(device) as draw:
            draw.text((x, 0), "Pulsioxímetro", font=font, fill="white")
            if hrm.bpm > 0:      
                draw.text((10, 25), f"Heart Rate: {int(hrm.bpm)} BPM", fill="white")
                draw.text((10, 40), f"SpO2: {int(hrm.spo2)}%", fill="white")
                insert_medicion(hrm.bpm, hrm.spo2)
                led_verde.on()
                led_rojo.off()
            else:
                draw.text((x1, 35), "Dedo no detectado", fill="white")
                led_verde.off()
                led_rojo.on()

def monitor_heart_rate_and_spo2():
    hrm = HeartRateMonitor(print_raw=False, print_result=False)
    hrm.start_sensor()

    try:
        print("Monitoreo de la frecuencia cardíaca y oxigenación iniciado. Presiona CTRL+C para detener. Presiona el botón para iniciar/detener el monitoreo.")
        while True:
            if sistema_encendido:
                display_sensor_data(hrm)
            else:
                led_verde.off()  # Apaga el LED verde
                led_rojo.off()  # Apaga el LED rojo
            time.sleep(0.5)  # Espera medio segundo antes de leer el siguiente valor
    except KeyboardInterrupt:
        print("Deteniendo el monitoreo...")
    finally:
        hrm.stop_sensor()
        led_verde.off()  # Apaga el LED verde
        led_rojo.off()  # Apaga el LED rojo

if __name__ == "__main__":
    monitor_heart_rate_and_spo2()