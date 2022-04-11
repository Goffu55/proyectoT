
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

class UserFind:
    
    def search(palabra):
        i = 0
        listaB = []
        while i < len(usuarios):
            busqueda = palabra in usuarios[i].values()
            listaB.append(busqueda)
            
            if (busqueda == True):
                print("id: " + usuarios[i]['id'])
                print("Nombre: " + usuarios[i]['nombre'])
                print("Apellido: " + usuarios[i]['apellido'])
                print("Correo: " + usuarios[i]['email'])
                if(palabra == "Manizales" or palabra == "Colombia"):
                    print("Pais: " + usuarios[i]['pais'])
                    print("Ciudad: " + usuarios[i]['ciudad'])
                print()
                i += 1    
            else:
                i += 1
        if(listaB.count(True) == 0):
            print(f'la palabra "{palabra}" no fue encontrada')
palabra = "ocampo"
UserFind.search(palabra)

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
class ProductFind:
    
    def search(palabra):
        i = 0
        j = 0
        listaB = []
        while i < len(usuarios):
           
            if len(usuarios[i]['productos']) > 0:
                busqueda = palabra in usuarios[i]['productos'][j]["nombre_product"]
                listaB.append(busqueda)
                
                if (busqueda == True):
                    print("id: " + usuarios[i]['productos'][i]['id'])
                    print("nombre product: " + usuarios[i]['productos'][i]['nombre_product'])
                    print("descripcion product: " + usuarios[i]['productos'][i]['descripcion_product'])
                    print("categoria: " + usuarios[i]['productos'][i]['categoria'])
                    print("precio: " + usuarios[i]['productos'][i]['price'])
                    i += 1
                    break
                else:
                    j += 1
            if(listaB.count(True) == 0):
                print(f'la palabra "{palabra}" no fue encontrada')

palabra = "miguelon3,0"
print(ProductFind.search(palabra))


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


