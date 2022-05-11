class enpilarCategoria: 

    # //////// PILA ////////

    # Declaramos la lista
    def __init__(self):
        self.datos = ["diseño", "programacion", "educacion"]
    
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

numeros = enpilarCategoria()
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.insertar("arte") # Inserta un nueva Categoria
numeros.insertar("musica") # Inserta un nueva Categoria
numeros.insertar("entretenimiento") # Inserta un nueva Categoria
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.extraer() # Sacamos ultima Categoria
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
numeros.extraer() # Sacamos ultima Categoria
numeros.extraer() # Sacamos ultima Categoria
print(numeros.datos) # Enlistamos los datos
print(numeros.cantidad()) # Consulta la cantidad de datos
