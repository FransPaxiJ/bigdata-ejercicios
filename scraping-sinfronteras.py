#%pip install bs4
import requests
from bs4 import BeautifulSoup
import re
import csv # esta librería nos permite escribir o crear archivos csv
import codecs # para manejar la codificacion (utf-8) de nuestro archivo csv

# semilla
url = 'https://diariosinfronteras.com.pe/category/puno/'
response = requests.get(url)

# Creamos un objeto BeautifulSoup para parsear el contenido
# del contenido de la página a un formato mas legible y manejable
html = BeautifulSoup(response.content, 'html.parser')

# Buscamos todas las secciones que contienen las noticias
seccion = html.find_all('li', class_='infinite-post')
#print(secciones)

# Iteramos sobre cada sección para obtener el título y la descripción
for element in seccion:
    # Obtenemos el titulo que esta dentro de la etiqueta h2
    titulo = element.find('h2').text
    # Obtenemos la descripción que esta dentro de la etiqueta p
    descripcion = element.find('p').text
    # Obtenemos el src que esta dentro de la etiqueta img
    img_tag = element.find('a').get('href')
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

# Escribimos los datos en un archivo csv llamado noticias_sf.csv
with codecs.open('noticias_sf.csv', 'w', 'utf-8-sig') as csvfile:
    # csvWriter es un objeto que nos permite escribir en el archivo csv
    csvWriter = csv.writer(csvfile, delimiter='|')
    # Escribimos la cabecera del archivo csv
    csvWriter.writerow(['Fecha', 'Titulo', 'Resumen'])

    # Iteramos sobre cada sección para obtener el título, la descripción y la fecha
    for secciones in seccion :
        # Obtenemos el titulo que esta dentro de la etiqueta h2
        titulo = secciones.find("h2").text
        # Obtenemos la descripción que esta dentro de la etiqueta p
        resumen = secciones.find("p").text

        # Obtenemos el enlace que esta dentro de la etiqueta a
        enlace = secciones.find("a")
        # Obtenemos el href que esta dentro de la etiqueta a
        c_href = enlace.get("href")
        # Buscamos la fecha en el enlace
        f_math = re.search(r'\d{4}/\d{2}/\d{2}', c_href)
        # Se encuen
        dfecha = f_math.group()
        csvWriter.writerow([dfecha, titulo, resumen])
    