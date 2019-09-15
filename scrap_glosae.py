"""
Proyecto: Glosae digitalibus
Autor: Jairo A. Melo Flórez
Fecha: septiembre 2019

Recupera la información de las glosas y las guarda en un archivo de texto separado por obra.
El nombre del archivo se guarda de acuerdo con el criterio utilizado por el proyecto
La Escuela de Salamanca
"""

import codecs
import os
import time

import requests

from get_glosa import glosa
from get_glosa import salsa
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

'''
prepara la sopa :D
'''

sopa = salsa(url)

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
            sopa_destino = salsa(link_destino)
            # Hallar la tabla de contenido para iterar la búsqueda
            # TODO: Este método regresa la información repetida.
            #  Es necesario corregir esto, tal vez haciendo un llamado a la página completa. Probar con request-html
            #  o Selenium.
            for tabla in sopa_destino.find_all('ul', class_='dropdown-menu scrollable-menu'):
                for enlaces in tabla.find_all('a'):
                    print(enlaces.text)  # La página de las glosas (no la agregamos al archivo de texto)
                    enlace_final = enlaces.get('href')
                    link_final = "{}{}".format(base_url, enlace_final)
                    try:
                        texto_glosa = glosa(link_final)
                        guardar_en.write(texto_glosa)
                    except requests.exceptions.RequestException as e:
                        print(e)
                        guardar_en.close()
                        os.remove(ruta_archivo)  # Eliminamos el archivo para evitar descargas incompletas
                    except requests.exceptions.ConnectionError as e:
                        print(e)
                        time.sleep(25)
                        pass

        except TypeError:
            guardar_en.close()
            os.remove(ruta_archivo)

        guardar_en.close()

    else:
        print("El archivo ya fue descargado")
