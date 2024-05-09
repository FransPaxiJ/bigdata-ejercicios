import matplotlib.pyplot as plt
import numpy as np

# Generamos los datos para el gráfico
eje_x = np.arange(-10, 10, 0.25)  # Este será nuestro eje x
y1 = np.sin(eje_x)  # Esta será la línea roja
y2 = np.cos(eje_x)  # Esta será la línea azul

# Creamos el gráfico
plt.figure(figsize=(10, 4))
plt.plot(eje_x, y1, color='red', label='Seno')  # Añadimos la etiqueta 'Seno' a la línea roja
plt.plot(eje_x, y2, color='blue', label='Coseno')  # Añadimos la etiqueta 'Coseno' a la línea azul

# Añadimos algunos detalles al gráfico
plt.title('Grafico de Coseno y Seno')
plt.xlabel('Eje X')
plt.ylabel('Amplitud')
plt.grid(True)

# Añadimos la leyenda al gráfico
plt.legend()

# Mostramos el gráfico
plt.show()