from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont

# Configuración del bus I2C y dirección del dispositivo OLED
serial = i2c(port=1, address=0x3C)

# Inicialización del dispositivo OLED con el controlador SH1106
device = sh1106(serial)

# Mensaje a mostrar
mensaje = "Hola, mundo!"

# Crear una imagen
image = Image.new("1", (device.width, device.height))
draw = ImageDraw.Draw(image)

# Fuente para el mensaje
font = ImageFont.load_default()

# Dibujar el mensaje en la imagen
draw.text((0, 0), mensaje, fill="white", font=font)

# Mostrar la imagen en la pantalla
device.display(image)
