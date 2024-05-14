# Importamos la clase Image de la biblioteca PIL para trabajar con imágenes
from PIL import Image
# Importamos la biblioteca time para medir el tiempo de ejecución
import time
# Importamos la biblioteca os para interactuar con el sistema operativo
import os

# Definimos la función Convertir que toma dos argumentos: la ruta de las imágenes originales y la ruta donde se guardarán las imágenes convertidas
def Convertir(ruta_original, ruta_destino):
    # Guardamos el tiempo de inicio
    inicio = time.time()
    # Obtenemos una lista de todos los archivos en la carpeta original
    archivos = os.listdir(ruta_original)
    # print (archivos) output: ['imagen1.jpg', 'imagen2.jpg', 'imagen3.jpg', 'imagen4.jpg', 'imagen5.jpg']
    # Iteramos sobre cada archivo en la lista de archivos
    for archivo in archivos:
        # Image.open abre la imagen en la ruta especificada
        imagen = Image.open(ruta_original+archivo)
        # print(image) output: <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1920x1080 at 0x7F3D3D3D3D90>
        # image.height devuelve la altura de la imagen en píxeles
        alto_original=imagen.height
        # print(alto_original) output: 1080
        # imagen.height devuelve el ancho de la imagen en píxeles
        ancho_original=imagen.width
        # print(ancho_original) output: 1920
        # imagen.width devuelve el ancho de la imagen en píxeles
        # ---------------------------------------------------------
        # Redimensionamos la imagen a la mitad de su tamaño original
        # Para ello, dividimos el ancho y el alto originales por 2
        # La función resize toma una tupla (ancho, alto), por lo que pasamos los nuevos valores como una tupla
        redimensionada = imagen.resize((int(ancho_original/2), int(alto_original/2)))
        # print(redimensionada) output: <PIL.Image.Image image mode=RGB size=960x540 at 0x7F3D3D3D3D90>
        # ---------------------------------------------------------
        # Guardamos la imagen en la ruta de destino, con una calidad de 25 (el valor por defecto es 75)
        redimensionada.save(ruta_destino+archivo, quality=25)
        # declaramos la variable fin, que guarda el tiempo actual
    # Calculamos el tiempo que tardó en terminar el ciclo
    fin = time.time()
    # Calculamos el tiempo que tardó en convertir la imagen
    tiempo_usado = fin-inicio
    print("Las conversiones tardaron", tiempo_usado, "segundos")
# Llamamos a la función Convertir con la ruta de las imágenes originales y la ruta donde queremos guardar las imágenes convertidas
Convertir("originales/", "convertidos/")