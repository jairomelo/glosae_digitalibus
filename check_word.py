"""
Proyecto: Glosae digitalibus
Autor: Jairo A. Melo Flórez
Fecha: septiembre 2019

Esta será una función que buscará nombres específicos en el texto.
"""
import codecs

'''
La función encuentrapalabra() regresa 
'''


def encuentrapalabra(nomarchivo, listapalabras):
    try:
        archivo = codecs.open(nomarchivo, 'r', 'utf-8')
        leer = archivo.readlines()
        archivo.close()

        for palabra in listapalabras:
            count = 0
            for oracion in leer:
                linea = oracion.split()
                for palabras in linea:
                    lineas = palabras.strip("&§¶ꝰ⁊ꝟ")
                    if palabra == lineas:
                        count += 1
        if count == 0:
            pass
        else:
            print(palabra, ":", count)
    except FileExistsError as e:
        print(e)
    except UnicodeDecodeError as e:
        print("El archivo no fue codificado en utf-8")
