from numpy import sort
from clientes import usuarios
import json
from flask import jsonify
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