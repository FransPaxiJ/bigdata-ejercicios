# importamos la libreria matplotlib, para crear 2 graficos en una misma figura
import matplotlib.pyplot as plt
import numpy as np

# Creamos una figura y un grafico, con un tamaño de 6x6 pulgadas
fig, graficos = plt.subplots(figsize=(8, 6))

# Graficamos una funcion cuadratica en el segundo grafico, con valores desde -10 a 10, de 0.25 en 0.25
# Para ellos nos apoyamos en numpy y su funcion arange
eje_x = np.arange(-10, 10, 0.25)

eje_y = [] # aqui guardaremos el valor de la funncion seno, para cada elemento de eje_x
for numero in eje_x:
    vseno = np.sin(numero) # calculamos el seno de cada elemento de eje_x
    eje_y.append(vseno) # guardamos el valor del seno en la lista eje_y
    print(vseno)

# Graficamos en el segundo grafico los puntos x y y, scatter es para graficar puntos
graficos.plot(
    eje_x,  # x values
    eje_y,  # y values
)

# Mostramos el grafico
plt.show()