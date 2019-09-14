import codecs
import os

import requests
from bs4 import BeautifulSoup

from get_glosa import glosa
from get_glosa import titulo

'''
Asegurarse de que el directorio para guardar los archivos existe
'''

directorio = "obras_ES"

if not os.path.exists(directorio):
    try:
        os.mkdir(directorio)
    except OSError as e:
        print(e)

'''
Enlaces base y prueba de conexión
'''

base_url = "https://www.salamanca.school/es/"

url = "{}works.html".format(base_url)

try:
    resultado = requests.get(url)
except requests.exceptions.HTTPError:
    raise

contenido = resultado.content

'''
prepara la sopa :D
'''

sopa = BeautifulSoup(contenido, 'xml')

for columnas in sopa.find_all('a', class_="lead"):  # Hallar los enlaces (as usual)
    enlace = columnas.get('href')
    nombrearchivo = enlace[14:19]
    print(nombrearchivo)
    # Cear texto para guardar las glosas, por obra

    ruta_archivo = "{}/{}.txt".format(directorio, nombrearchivo)

    if not os.path.exists(ruta_archivo):
        guardar_en = codecs.open(ruta_archivo, 'a', 'utf-8')

        #  Construir los enlaces
        link_destino = "{}{}".format(base_url, enlace)
        print(link_destino)
        guardar_en.write(link_destino)

        #  Identificar el título
        titul = titulo(link_destino)
        print(titul)
        try:
            guardar_en.write(titul)

            #  Scraping de la página de destino (por elemento del índice)
            obtener_destino = requests.get(link_destino)
            contenido_destino = obtener_destino.content
            sopa_destino = BeautifulSoup(contenido_destino, 'xml')
            # Intentamos hallar la tabla de contenido. Si no la encuentra, no regresa nada :D
            for tabla in sopa_destino.find_all('ul', class_='dropdown-menu scrollable-menu'):
                for enlaces in tabla.find_all('a'):
                    print(enlaces.text)  # La página de las glosas (no la agregamos al texto)
                    enlace_final = enlaces.get('href')
                    link_final = "{}{}".format(base_url, enlace_final)
                    try:
                        texto_glosa = glosa(link_final)
                        guardar_en.write(texto_glosa)
                    except requests.exceptions.RequestException as e:
                        print(e)
        except TypeError:
            guardar_en.close()
            os.remove(ruta_archivo)

        guardar_en.close()

    else:
        print("El archivo ya fue descargado")
