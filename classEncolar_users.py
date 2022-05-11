from clientes import usuarios

# //////// COLA ////////
class users:
    # Declaramos la lista
    def __init__(self):
        self.datos = list(usuarios)
    
    # Consultamos la cantidad de elementos de la lista 
    def cantidad(self):
        return len(self.datos)
    
    # Insertamos un nuevo elemento a la lista y la posicionamos en la ultima posición
    def insertar(self, dato):
        if self.cantidad() == 0:
            self.datos.insert(0, dato)
        else:
            self.datos.insert(self.cantidad() + 1, dato)
    
    # Sacamos el ultimo elemento ingresado a la lista
    def extraer(self):
        if self.cantidad():
            return self.datos.pop(0)
        else:
            return None
    
    # Consultamos el primer dato
    def primer_dato(self):
        if self.cantidad():
            return self.datos[-1]
    
    # Consultamos el ultimo dato
    def ultimo_dato(self):
        if self.cantidad():
            return self.datos[0]

numeros = users()
new1 = {
    "id": "9",
    "nombre": "Ginna",
    "apellido": "Tangarife",
    "username": "Ginnalaenculada",
    "phone": 3123456278,
}

new2 = {
    "id": "2",
    "nombre": "Sergio",
    "apellido": "Diaz",
    "username": "SergioD",
    "phone": 3116678233
}


new3 = {
    "id": "2",
    "nombre": "Juan Diego",
    "apellido": "Agudelo",
    "username": "AgudeloJD",
    "phone": 3012334567
}




print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.insertar(new1) # Inserta un nuevo producto
numeros.insertar(new2) # Inserta un nuevo producto
numeros.insertar(new3) # Inserta un nuevo producto
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.extraer() # Sacamos ultmo producto
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.extraer() # Sacamos ultmo producto
numeros.extraer() # Sacamos ultmo producto
numeros.extraer() # Sacamos ultmo producto
numeros.insertar(new1) # Inserta un nuevo producto
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos