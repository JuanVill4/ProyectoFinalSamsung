from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont
import psutil
from pathlib import Path
import time


# Inicialización del bus I2C y dirección del dispositivo OLED
serial = i2c(port=1, address=0x3C)

# Inicialización del dispositivo OLED con el controlador SH1106
device = sh1106(serial, rotate=0)

# Ruta de la fuente personalizada
font_path = str(Path(__file__).resolve().parent.joinpath('fonts', 'C&C Red Alert [INET].ttf'))

# Función para convertir bytes a unidades legibles por humanos
def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = int(float(n) / prefix[s])
            return '%s%s' % (value, s)
    return "%sB" % n

# Función para obtener el uso de la memoria
def mem_usage():
    usage = psutil.virtual_memory()
    return "Memoria: %s %.0f%%" % (bytes2human(usage.used), 100 - usage.percent)

# Función para obtener el uso del disco
def disk_usage(dir):
    usage = psutil.disk_usage(dir)
    return "SD:  %s %.0f%%" % (bytes2human(usage.used), usage.percent)

# Bucle principal para actualizar la pantalla cada 10 segundos
while True:
    # Limpiar la pantalla y mostrar el estado de la Raspberry Pi
    with canvas(device) as draw:
        draw.text((5, 0), "Raspberry PI Status", fill="white")
        draw.text((5, 6), "-------------------", fill="white")
        draw.text((0, 16), mem_usage(), fill="white", font=ImageFont.truetype(font_path, 12))
        draw.text((0, 30), disk_usage('/'), fill="white", font=ImageFont.truetype(font_path, 12))
        draw.text((9, 50), "www.firtec.com.ar", fill="white", font=ImageFont.truetype(font_path, 12))
    
    # Esperar 10 segundos antes de la próxima actualización
    time.sleep(10)
