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

nombres = ["Aristóteles", "Aristoteles", "Arist.", "Ari.", "Ethicorum", "Ethico."]

for archivo in archivos:
    print("Resultados encontrados en {}:".format(archivo))
    for autores in nombres:
        try:
            encuentrapalabra(archivo, [autores])
        except FileExistsError as e:
            print(e)
