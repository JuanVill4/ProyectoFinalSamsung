
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import Image
# Ruta de la imagen PBM
image_path = "/home/juanv/Documents/ProyectoSamsung/ProyectoFinalSamsungEquipo10/Imagenes/heart.pbm"

# Cargar la imagen desde un archivo PBM
with open(image_path, "rb") as f:
    image_data = f.read()

# Mostrar la imagen en el display
with canvas(sh1106) as draw:
    draw.bitmap((0, 0), image_data, fill="white")

