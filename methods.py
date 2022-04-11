from ctypes.wintypes import WORD
from itertools import count, product
from math import prod
from platform import java_ver
from select import select
from unicodedata import category
from clientes import usuarios

# print(len(usuarios))

# Crear un usuario
def addusuario():
    new_usuario = {
        "id": "4",
        "nombre": "Fico",
        "apellido": "escobar",
        "username": "carlitos123",
        "phone": 3015605651,
        "identificacion": 1010148638,
        "email": "carlitosescobar@gmail.com",
        "password": "carlon123",
        "pais": "Colombia",
        "ciudad": "Manizales",
        "direccion": "cll58f#8-48",
        "fech_nac": "08-01-2001",
        "fech_init": "01-03-2022",
        "descripcion": "Hola, soy desarrollador junior, inspirado por el aprendisaje",
        "datos_estra": {
            "habilidades": "qefbnofuwr",
            "educacion": "Chimbis",
            "certificacion": "good",
        },
        "product": []
    }
    usuarios.append(new_usuario)
    # print(len(usuarios))
addusuario()

# Actualizar usuario

# print("ingrese el id del usuario: ")
# NoID =  input()

# print("Qué dato desea actualizar: ")
# print(usuarios[1].keys())
# val_upd = input()

# print("ingese el nuevo valor")
# new_val = input()

def updUsuario( Numid,valUpd, newVal ):
    i = 0
    listaB = []

    while i < len(usuarios):
        busqueda = Numid in usuarios[i]["id"]
        listaB.append(busqueda)
        if (busqueda == True):
            usuarios[i].update({valUpd: newVal})
            print(usuarios[i])
            i += 1    
        else:
            i += 1
    if(listaB.count(True) == 0):
        print(f'la id "{Numid}" no fue encontrada')

# updUsuario(NoID, val_upd, new_val)

# Eliminar usuario

# print("ingrese el id del usuario a Eliminar: ")
# NoID =  input()

def delUsuario( Numid ):
    i = 0
    listaB = []

    while i < len(usuarios):
        busqueda = Numid in usuarios[i]["id"]
        listaB.append(busqueda)
        if (busqueda == True):
            usuarios.pop(i)
            # print(usuarios[i])
            i += 1    
        else:
            i += 1
    if(listaB.count(True) == 0):
        print(f'la id "{Numid}" no fue encontrada')

# delUsuario(NoID)


#Sort a codigo

lista = []

def generarListaNombre():
    i = 0
    while i < len(usuarios):
        elemento = usuarios[i]['nombre']
        lista.append(elemento)
        i +=1
    return lista
print(generarListaNombre())
lista2=[]
def quicksort(generarListaNombre):
    if not generarListaNombre:
        return []
    return (quicksort([x for x in generarListaNombre[1:] if x <  generarListaNombre[0]])
            + [generarListaNombre[0]] +
            quicksort([x for x in generarListaNombre[1:] if x >= generarListaNombre[0]]))
print(quicksort(lista))
print()

#Sort a codigo de la Z-A

# def quicksortR(generarListaNombre):
#     if not generarListaNombre:
#         return []
#     return (quicksortR([x for x in generarListaNombre[:1] if x <=  generarListaNombre[0]])
#              [generarListaNombre[0]] +
#             quicksortR([x for x in generarListaNombre[:1] if x > generarListaNombre[0]]))
# print(quicksortR(lista))
# print()

# Search a codigo

palabra = "ocampo"
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
        

# search(palabra)

def contarUsuarios():    
    print("El numero de Usuarios es: ")
    print(len(usuarios))
    print()

# contarUsuarios()

# Crear producto
# print("ingrese el id del usuario: ")
# NoID2 =  input()
# cont = len(usuarios[0]["productos"])
# print("ingrese el nombre del producto: ")
# product_name = input()
# print("ingrese la descripcion del producto: ")
# product_desc = input()
# print("ingrese la categoria del producto: ")
# product_category = input()
# print("ingrese la precio del producto: ")
# product_price = input()
# new_productos={
#     "id": int(cont) + 1,
#     "nombre_product": product_name,
#     "descripcion_product": product_desc,
#     "categoria": product_category,
#     "price": product_price,
#     "estrellas": 0
# }
# NoID3 =  NoID2
def createProduct( idUser ):
    i = 0
    listaB = []

    while i < len(usuarios):
        busqueda = idUser in usuarios[i]["id"]
        listaB.append(busqueda)
        if (busqueda == True):
            usuarios[i]["productos"].append(new_productos)
            print(usuarios[i]["productos"])
            i += 1    
        else:
            i += 1
    if(listaB.count(True) == 0):
        print(f'la id "{idUser}" no fue encontrada')

# createProduct(NoID2)

# Actualizar producto

# print("ingrese el id del usuario: ")
# NoID3 =  input()
# cont = len(usuarios[0]["productos"])
# print("ingrese el id del producto: ")
# product_id = input()
# print("ingrese el campo del producto a cambiar: ")
# product_detalis = input()
# print("ingrese el valor del campo a cambiar: ")
# product_value = input()

# NoID4 = NoID3
def updtProduct( idUser,  product_id):
    i = 0
    listaB = []

    while i < len(usuarios):
        busqueda = idUser in usuarios[i]["id"]
        listaB.append(busqueda)
        if (busqueda == True):
            j = 0
            while j < len(usuarios[i]["productos"]):
                busqueda2 = product_id in usuarios[i]["productos"][j]["id"]
                if (busqueda2 == True):
                    usuarios[i]["productos"][j].update({product_detalis: product_value})
                    j += 1
                else:
                    j += 1
            print(usuarios[i]["productos"])
            i += 1    
        else:
            i += 1
    if(listaB.count(True) == 0):
        print(f'la id "{idUser}" no fue encontrada')

# updtProduct(NoID4, product_id)

# Eliminar producto

# print("ingrese id del usuario")
# NoUser = input()

# print("ingrese id del producto")
# NoProd = input()

def delProduct( NoUser, NoProd ):
    i = 0
    listaB = []
    while i < len(usuarios):
        busqueda = NoUser in usuarios[i]["id"]
        listaB.append(busqueda)
        if (busqueda == True):
            j = 0
            while j < len(usuarios[i]["productos"]):
                busqueda2 = NoProd in usuarios[i]["productos"][j]["id"]
                if (busqueda2 == True):
                    usuarios[i]["productos"].pop(j)
                    print(usuarios[i]["productos"])
                    j += 1
                else:
                    j += 1
            print(usuarios[i]["productos"])
            i += 1    
        else:
            i += 1
    if(listaB.count(True) == 0):
        print(f'la id "{NoUser}" no fue encontrada')

# delProduct(NoUser, NoProd)

#Sort a codigo producto

# listas = []
# print(len(usuarios[0]["productos"]))

# def generarListaProducto():
#     i = 0
#     j = 0
#     while i < len(usuarios):
#         while j < len(usuarios[i]["productos"]):
#             elemento = usuarios[i]["productos"][j]["nombre_product"]
#             if (elemento == ""):
#                 listas.append(elemento)
#             j += 1
#         i +=1
#     return listas
# print(generarListaProducto())
# def quicksort(generarListaProducto):
#     if not generarListaProducto:
#         return []
#     return (quicksort([x for x in generarListaProducto[1:] if x <  generarListaProducto[0]])
#             + [generarListaProducto[0]] +
#             quicksort([x for x in generarListaProducto[1:] if x >= generarListaProducto[0]]))
# print(quicksort(lista))
# print(usuarios[0]['productos'][0]["nombre_product"])

