from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont
import time

# Inicialización del bus I2C y dirección del dispositivo OLED
serial = i2c(port=1, address=0x3C)

# Inicialización del dispositivo OLED con el controlador SH1106
device = sh1106(serial)
ancho_display, alto_display = 128, 64

# Carga tu fuente bonita aquí. Asegúrate de tener el archivo de fuente en el mismo directorio que tu script
# O ajusta la ruta al directorio correcto donde se encuentra tu fuente.
font_path = "ProyectoFinalSamsungEquipo10/Code/templates/Starjedi.ttf"
font_path1 = "ProyectoFinalSamsungEquipo10/Code/templates/ALBA____.TTF"
font = ImageFont.truetype(font_path, 12)  # Ajusta el tamaño de la fuente según necesites
font1 = ImageFont.truetype(font_path1, 18)  # Ajusta el tamaño de la fuente según necesites

with canvas(device) as draw:
        # draw.text((0, 0), "Pulsioximetro", font=font , fill="white", align='center')
        # draw.text((10, 30), "Frecuencia Cardiaca:", font=font1, fill="white")

        # draw.text((10, 40), "Oxigeno en sangre:", font=font1, fill="white")
         
        # Calculando el ancho y alto del texto
        ancho_texto, alto_texto = draw.textsize("Pulsioximetro", font=font1)
        
        # Calculando el punto medio del display
        ancho_display, alto_display = device.width, device.height
        
        # Ajustando las coordenadas x, y para centrar el texto
        x = (ancho_display - ancho_texto) / 2
        # Para centrar verticalmente, puedes ajustar 'y' de manera similar, o usar una posición fija si prefieres
        y = (alto_display - alto_texto) / 2  # Ajusta esto según la línea específica donde quieras mostrar el texto


while True:

    with canvas(device) as draw:
        # draw.text((0, 0), "Pulsioximetro", font=font , fill="white", align='center')
        # draw.text((10, 30), "Frecuencia Cardiaca:", font=font1, fill="white")

        # draw.text((10, 40), "Oxigeno en sangre:", font=font1, fill="white")
         
        # # Calculando el ancho y alto del texto
        # ancho_texto, alto_texto = draw.textsize("Pulsioximetro", font=font1)
        
        # # Calculando el punto medio del display
        # ancho_display, alto_display = device.width, device.height
        
        # # Ajustando las coordenadas x, y para centrar el texto
        # x = (ancho_display - ancho_texto) / 2
        # # Para centrar verticalmente, puedes ajustar 'y' de manera similar, o usar una posición fija si prefieres
        # y = (alto_display - alto_texto) / 2  # Ajusta esto según la línea específica donde quieras mostrar el texto
        
        # Dibujando el texto centrado
        draw.text((x, 0), "Pulsioximetro", font=font1, fill="white")

        draw.text((10, 25), "Heart Rate:", fill="white")

        draw.text((10, 40), "Sp02:", fill="white")
        
        
        
        