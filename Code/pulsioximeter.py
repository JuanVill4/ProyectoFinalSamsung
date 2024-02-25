from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
import time
from Pulsioximeter import max30102, hrcalc


# Inicialización del bus I2C y dirección del dispositivo OLED
serial = i2c(port=1, address=0x3C)

# Inicialización del dispositivo OLED con el controlador SH1106
device = sh1106(serial, rotate=0)

# Inicialización del sensor MAX30102
m = max30102.MAX30102()

# Función para obtener la frecuencia cardíaca y la saturación de oxígeno del sensor MAX30102
def get_hr_and_spo2():
    red, ir = m.read_sequential()
    hr, hrb, sp, spb = hrcalc.calc_hr_and_spo2(ir, red)
    return hr, sp

# Bucle principal para actualizar la pantalla cada 10 segundos
while True:
    # Limpiar la pantalla
    with canvas(device) as draw:
        # Obtener la frecuencia cardíaca y la saturación de oxígeno
        hr, sp = get_hr_and_spo2()
        
        # Mostrar la frecuencia cardíaca y la saturación de oxígeno
        draw.text((0, 0), f"Heart Rate: {hr} bpm", fill="white")
        draw.text((0, 16), f"SpO2: {sp}%", fill="white")
        
    # Esperar 10 segundos antes de la próxima actualización
    time.sleep(1)
