from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image

# Inicialización del bus I2C y dirección del dispositivo OLED
serial = i2c(port=1, address=0x3C)

# Inicialización del dispositivo OLED con el controlador SH1106
device = sh1106(serial, rotate=0)

# Ruta de la imagen PBM
image_path = 'Imagenes/heart.pbm'  # Asegúrate de cambiar esto por la ruta real de tu imagen

# Cargar la imagen PBM
image = Image.open(image_path)

# Redimensionar la imagen al tamaño de la pantalla OLED si es necesario
# Esto asume que la resolución del dispositivo es 128x64. Ajusta según tu dispositivo.
image_resized = image.resize(device.size)

# Mostrar la imagen en el dispositivo OLED
device.display(image_resized)
