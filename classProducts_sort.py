from numpy import sort
from clientes import usuarios
import json
from flask import jsonify
class products_sort:

    def generarListaProducto():
        listas = []

        i = 0
        while i < len(usuarios):
            j = 0
            while j < len(usuarios[i]["productos"]):
                elemento = usuarios[i]['productos'][j]["categoria"]
                listas.append(elemento)
                j += 1
            i +=1
        return listas

listass = products_sort.generarListaProducto()

def quicksort(generarListaProducto):
    if not generarListaProducto:
        return []
    return (quicksort([x for x in generarListaProducto[1:] if x <  generarListaProducto[0]])
            + [generarListaProducto[0]] +
            quicksort([x for x in generarListaProducto[1:] if x >= generarListaProducto[0]]))

print(quicksort(listass))