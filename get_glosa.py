"""
Proyecto: Glosae digitalibus
Autor: Jairo A. Melo Flórez
Fecha: septiembre 2019

Tres funciones que recuperan información específica de las glosas del proyecto Salamanca y el título de la obra.
También aprovecho la función `salsa()` para recuperar la información con requests y BeautifulSoup
sin tener que hacerlo varias veces en el mismo script.
"""

import requests
from bs4 import BeautifulSoup

'''
Hace la salsa, para evitar hacerla cada rato
'''


def salsa(url):
    re = requests.get(url)
    cont = re.content

    return BeautifulSoup(cont, 'lxml')


'''
Regresa un texto con las glosas, separadas por comas.
'''


def glosa(url):
    textos = []

    sopa = salsa(url)

    for span in sopa.find_all('span',
                              class_='original abbr unsichtbar'):  # Retirar las etiquetas modernizadoras del texto
        span.extract()

    for notas in sopa.find_all('span', class_='note-paragraph'):
        textos.append(notas.text)

    lista_def = [item.replace('\n', '') for item in textos]

    texto = ",".join(lista_def)

    return texto


'''
Regresa el título :D
'''


def titulo(url):
    sopa = salsa(url)

    for titulo_obra in sopa.find_all('h4'):
        for tit in titulo_obra.find_all('a'):
            rtit = tit.get('title')
            tit_final = rtit.replace('(Go to top of)', '')
            return tit_final
