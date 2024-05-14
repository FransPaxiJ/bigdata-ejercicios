# Importamos la clase Image de la biblioteca PIL para trabajar con imágenes
from PIL import Image
# Importamos la biblioteca time para medir el tiempo de ejecución
import time
# Importamos la biblioteca threading para poder crear hilos
import threading
# Importamos la biblioteca os para interactuar con el sistema operativo
import os

# Definimos la función ConvertirUnico que toma tres argumentos: la ruta de las imágenes originales, la ruta donde se guardarán las imágenes convertidas y el nombre del archivo
def ConvertirUnico(ruta_original, ruta_destino, archivo):
    # Abrimos la imagen original
    redimensionada = Image.open(ruta_original+archivo)
    # print(redimensionada) output: <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1920x1080 at 0x7F3D3D3D3D90>
    # ---------------------------------------------------------
    # Obtenemos alto de la imagen original
    alto_original=redimensionada.height
    # Obtenemos el ancho de la imagen original
    ancho_original=redimensionada.width
    # Redimensionamos la imagen a la mitad de su tamaño original
    redimensionada = redimensionada.resize((int(ancho_original/2), int(alto_original/2)))
    # Guardamos la imagen en la ruta de destino, con una calidad de 25 (el valor por defecto es 75)
    redimensionada.save(ruta_destino+archivo, quality=25)

# Definimos la función Convertir que toma dos argumentos: la ruta de las imágenes originales y la ruta donde se guardarán las imágenes convertidas
def Convertir(ruta_original, ruta_destino):
    # Guardamos el tiempo de inicio
    inicio = time.time()
    # Obtenemos una lista de todos los archivos en la ruta original
    archivos = os.listdir(ruta_original)
    # Creamos una lista vacía para guardar los hilos
    HILOS = []

    for archivo in archivos:
        hilo = threading.Thread(target=ConvertirUnico, args=(ruta_original, ruta_destino, archivo))
        hilo.start()
        HILOS.append(hilo)
    
    for hilo in HILOS:
        hilo.join()

    fin = time.time()
    # Calculamos el tiempo que tardó en convertir la imagen
    tiempo_usado=fin-inicio
    # Imprimimos el tiempo que tardaron las conversiones
    print("Las conversiones tardaron", tiempo_usado, "segundos")

def contador_hilos():
    print("Hilos activos:", threading.active_count())

# Llamamos a la función Convertir con la ruta de las imágenes originales y la ruta donde queremos guardar las imágenes convertidas
Convertir("originales/", "convertidos/")