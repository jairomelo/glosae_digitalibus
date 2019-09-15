"""
Proyecto: Glosae digitalibus
Autor: Jairo A. Melo Flórez
Fecha: septiembre 2019

Script para buscar nombres y la cantidad de veces que aparecen citados en varios archivos.
"""
import os

from check_word import encuentrapalabra

try:
    from scandir import walk
except ImportError:
    walk = os.walk
'''
Función para identificar los archivos en el directorio obras_ES
'''


def buscartxt(directorio):
    listatxt = []

    for r, d, f in walk(directorio):
        for file in f:
            if '.txt' in file:
                listatxt.append(os.path.join(r, file))
    return listatxt


archivos = buscartxt('obras_ES')

nombres = ["Aristoteles", "Aristóteles", "Arist.", "Ari.", "Ethicorum", "Ethic."]

for archivo in archivos:
    try:
        print("Resultados para {}:".format(archivo))
        for autores in nombres:
            encuentrapalabra(archivo, [autores])
    except FileNotFoundError as e:
        print("{}. Posiblemente el nombre del archivo o la ruta está mal escrito.".format(e))
    except PermissionError:
        print("No se puede buscar en un directorio")
