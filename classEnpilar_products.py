from clientes import productos
class enpilarProducts:
    # //////// PILA ////////

    # Declaramos la lista
    def __init__(self):
        self.datos = list(productos)
    
    # Consultamos la Cantidad de eelementos en la lista 
    def cantidad(self):
        return len(self.datos)
    
    # Insertamos un nuevo elemento a la lista y la posicionamos en la ultima posición
    def insertar(self, dato):
        if self.cantidad() == 0:
            self.datos.insert(0, dato)
        if self.cantidad() != 0:
            self.datos.insert(self.cantidad() + 1, dato)
    
    # Sacamos el ultimio elemento ingresado a la lista
    def extraer(self):
        if self.cantidad():
            return self.datos.pop()
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

productnew1 = {
    "id": "3",
    "nombre_product": "ginnota2.0",
    "descripcion_product": "buena, bonita y cara",
    "categoria": "1",
    "price": "no tiene precio",
    "estrellas": 5
}

productnew2 = {
    "id": "4",
    "nombre_product": "sergiote",
    "descripcion_product": "serio y gracioso",
    "categoria": "3",
    "price": "1000",
    "estrellas": 4
}

productnew3 = {
        "id": "2",
        "nombre_product": "diegooooooos",
        "descripcion_product": "callado y serio",
        "categoria": "6",
        "price": "20000",
        "estrellas": 5
}


numeros = enpilarProducts()
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.insertar(productnew1) # Inserta un nuevo producto
numeros.insertar(productnew2) # Inserta un nuevo producto
numeros.insertar(productnew3) # Inserta un nuevo producto
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.extraer() # Sacamos ultmo producto
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.extraer() # Sacamos ultmo producto
numeros.extraer() # Sacamos ultmo producto
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos