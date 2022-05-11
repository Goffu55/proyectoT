from numpy import sort
from clientes import usuarios
import json
from flask import jsonify
class extra_sort:

    def generarListaestras():
        listas = []

        i = 0
        while i < len(usuarios):

            elemento = usuarios[i]['datos_estra']["Duravilidad_meses"]
            listas.append(elemento)

            i +=1
        return listas

listasss = extra_sort.generarListaestras()

def quicksort(generarListaProducto):
    if not generarListaProducto:
        return []
    return (quicksort([x for x in generarListaProducto[1:] if x <  generarListaProducto[0]])
            + [generarListaProducto[0]] +
            quicksort([x for x in generarListaProducto[1:] if x >= generarListaProducto[0]]))

print(quicksort(listasss))