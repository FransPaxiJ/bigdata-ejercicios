# importamos la libreria matplotlib, para crear 2 graficos en una misma figura
import matplotlib.pyplot as plt
import numpy as np
# Creamos una figura y un grafico, con un tamaño de 6x6 pulgadas
fig, graficos = plt.subplots(1,2,figsize=(8, 6))

# Graficamos en el primer grafico los puntos x y y, scatter es para graficar puntos
graficos[0].scatter(
    [1, 2, 3],  # x values
    [3, 2, 1],  # y values
)

# Graficamos una funcion cuadratica en el segundo grafico, con valores desde -10 a 10, de 0.25 en 0.25
# Para ellos nos apoyamos en numpy y su funcion arange
eje_x = np.arange(-10, 10, 0.25)
eje_y = [] # aqui guardaremos los valores cuadrado
for numero in eje_x:
    cuadrado = numero**2
    eje_y.append(cuadrado)

# Graficamos en el segundo grafico los puntos x y y, scatter es para graficar puntos
graficos[1].plot(
    eje_x,  # x values
    eje_y,  # y values
)

# Mostramos el grafico
plt.show()