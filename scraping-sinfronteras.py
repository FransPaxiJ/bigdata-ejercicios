#%pip install bs4
import requests
from bs4 import BeautifulSoup
import re

# semilla
url = 'https://diariosinfronteras.com.pe/category/puno/'
response = requests.get(url)

# Creamos un objeto BeautifulSoup para parsear el contenido
# del contenido de la página a un formato mas legible y manejable
html = BeautifulSoup(response.content, 'html.parser')

# Buscamos todas las secciones que contienen las noticias
secciones = html.find_all('li', class_='infinite-post')
#print(secciones)

# Iteramos sobre cada sección para obtener el título y la descripción
for secciones in secciones:
    # Obtenemos el titulo que esta dentro de la etiqueta h2
    titulo = secciones.find('h2').text
    # Obtenemos la descripción que esta dentro de la etiqueta p
    descripcion = secciones.find('p').text
    # Obtenemos el src que esta dentro de la etiqueta img
    img_tag = secciones.find('a').get('href')
    # -----------------------------------
    # Esto es expresiones regulares (regex) para buscar la fecha en la url de la imagen
    # Obtenemos la fecha que esta dentro de la etiqueta img
    # el {4} indica que se espera un número de 4 dígitos y el / indica que se espera un slash
    fecha = re.search(r'\d{4}/\d{2}/\d{2}', img_tag)
    # -----------------------------------
    # Si la fecha no es encontrada, se asigna un mensaje
    if fecha:
        fecha = fecha.group()
    else:
        fecha = "Fecha no encontrada"
    print("\n------------------\nTítulo: {}\nDescripción: {}\nFecha: {}\n------------------\n".format(titulo, descripcion, fecha))