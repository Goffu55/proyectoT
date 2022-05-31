class encolarMembresias: 
    # //////// COLA ////////

    # Declaramos la lista
    def __init__(self):
        self.datos = ["basic", "estandar", "premium"]
    
    # Consultamos la Cantidad de eelementos en la lista 
    def cantidad(self):
        return len(self.datos)
    
    # Insertamos un nuevo elemento a la lista y la posicionamos en la ultima posición
    def insertar(self, dato):
        if self.cantidad() == 0:
            self.datos.insert(0, dato)
        else:
            self.datos.insert(self.cantidad() + 1, dato)
    
    # Sacamos el ultimio elemento ingresado a la lista
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

numeros = encolarMembresias()
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.insertar("pro") # Inserta un nuevo plan
numeros.insertar("mega pro") # Inserta un nuevo plan
numeros.insertar("empresarial") # Inserta un nuevo plan
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.extraer() # Sacamos ultmo plan
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.extraer() # Sacamos ultmo plan
numeros.extraer() # Sacamos ultmo plan
numeros.extraer() # Sacamos ultmo plan
numeros.insertar("pro") # Inserta un nuevo plan
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.extraer() # Sacamos ultmo plan
numeros.extraer() # Sacamos ultmo plan
numeros.extraer() # Sacamos ultmo plan
numeros.extraer() # Sacamos ultmo plan
numeros.extraer() # Sacamos ultmo plan
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos