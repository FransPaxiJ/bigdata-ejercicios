# Importamos la biblioteca time para poder usar la función sleep
import time

# Importamos la biblioteca threading para poder crear hilos
import threading

# Definimos la función saludo que será ejecutada por cada hilo
def saludo(nombre):
    print(f"Hola, {nombre}")
    time.sleep(2)

# Creamos cuatro hilos, cada uno con la función saludo y un nombre diferente como argumento
hilo1 = threading.Thread(target=saludo, args=("Juan",))
hilo2 = threading.Thread(target=saludo, args=("Pedro",))
hilo3 = threading.Thread(target=saludo, args=("Ana",))
hilo4 = threading.Thread(target=saludo, args=("Patricia",))

# Iniciamos los cuatro hilos. Cada hilo ejecutará la función saludo con el nombre que le pasamos como argumento
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()

# Usamos join para esperar a que cada hilo termine antes de continuar con el resto del programa
hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()

# Imprimimos un mensaje final cuando todos los hilos han terminado
print("todos ya saludaron")