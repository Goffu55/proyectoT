from numpy import sort
from clientes import usuarios
import json
from flask import jsonify

class Users:
    def generarListaNombre():
        lista = []
        i = 0
        while i < len(usuarios):
            elemento = usuarios[i]['edad']
            lista.append(elemento)
            i +=1
        return lista

lista = Users.generarListaNombre()

def quicksort(generarListaNombre):
    if not generarListaNombre:
        return []
    return (quicksort([x for x in generarListaNombre[1:] if x <  generarListaNombre[0]])
            + [generarListaNombre[0]] +
            quicksort([x for x in generarListaNombre[1:] if x >= generarListaNombre[0]]))
print(quicksort(lista))









