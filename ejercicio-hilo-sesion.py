# Importamos la biblioteca time para poder usar la función sleep
import time

# Importamos la biblioteca threading para poder crear hilos
import threading

# Definimos la función saludo que será ejecutada por cada hilo
def conteo_hilos(numero_hilos):
    for i in range(numero_hilos):
        print(f"Contando {i}")
        time.sleep(1)

# Creamos cuatro hilos, cada uno con la función saludo y un nombre diferente como argumento
hilo1 = threading.Thread(target=conteo_hilos, args=(11,))
hilo2 = threading.Thread(target=conteo_hilos, args=(11,))
hilo3 = threading.Thread(target=conteo_hilos, args=(11,))
hilo4 = threading.Thread(target=conteo_hilos, args=(11,))
hilo5 = threading.Thread(target=conteo_hilos, args=(11,))
# Iniciamos los cuatro hilos. Cada hilo ejecutará la función saludo con el nombre que le pasamos como argumento
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo5.start()
# Usamos join para esperar a que cada hilo termine antes de continuar con el resto del programa
hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()
hilo5.join()
# Imprimimos un mensaje final cuando todos los hilos han terminado
print("termino de contar los hilos")