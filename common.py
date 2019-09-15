"""
Scripts comunes
"""

import os

try:
    from scandir import walk
except ImportError:
    walk = os.walk

'''
Buscar archivos en un directorio
'''


def buscartxt(directorio):
    listatxt = []

    for r, d, f in walk(directorio):
        for file in f:
            if '.txt' in file:
                listatxt.append(os.path.join(r, file))
    return listatxt
