import matplotlib.pyplot as plt
import numpy as np

# Generamos los datos para el gráfico
eje_x = np.arange(-10, 10, 0.25)  # Este será nuestro eje x
y_seno = np.sin(eje_x)  # Esta será la línea para la función seno
y_coseno = np.cos(eje_x)  # Esta será la línea para la función coseno
y_tangente = np.tan(eje_x)  # Esta será la línea para la función tangente
y_cuadratica = eje_x**2  # Esta será la línea para la función cuadrática

# Creamos una figura y un conjunto de gráficos, con un tamaño de 8x6 pulgadas
# 1 fila, 2 columnas
fig, graficos = plt.subplots(3, 6, figsize=(16, 4))

# Graficamos la función seno en el primer gráfico
graficos[0,0,0].plot(eje_x, y_seno, color='blue', label='Seno')  # Añadimos la etiqueta 'Seno' a la línea azul
graficos[0,0,0].legend()

# Graficamos la función coseno en el segundo gráfico
graficos[0,0,1].plot(eje_x, y_coseno, color='red', label='Coseno')  # Añadimos la etiqueta 'Coseno' a la línea roja
graficos[0,0,1].legend()

# Graficamos la función tangente en el tercer gráfico
graficos[0,0,2].plot(eje_x, y_tangente, label='Tangente')  # Añadimos la etiqueta 'Tangente' a la línea
graficos[0,0,2].legend()

# Graficamos la función cuadrática en el cuarto gráfico
graficos[1,0,0].plot(eje_x, y_cuadratica, label='prueba4')  # Añadimos la etiqueta 'Cuadrática' a la línea
graficos[1,0,0].legend()

# Graficamos la función cuadrática en el cuarto gráfico
graficos[1,1,0].plot(eje_x, y_cuadratica, label='prueba5')  # Añadimos la etiqueta 'Cuadrática' a la línea
graficos[1,1,0].legend()

# Graficamos la función cuadrática en el cuarto gráfico
graficos[1,1,1].plot(eje_x, y_cuadratica, label='prueba6')  # Añadimos la etiqueta 'Cuadrática' a la línea
graficos[1,1,1].legend()

# Mostramos el gráfico
plt.show()