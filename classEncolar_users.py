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
    "identificacion": 10027894533,
    "email": "gtplalokis@gmail.com",
    "password": "sebastianmivida",
    "pais": "Colombia",
    "ciudad": "Manizales",
    "direccion": "cll66c#45-89",
    "fech_nac": "12-01-2001",
    "fech_init": "08-04-2022",
    "descripcion": "Hola, soy desarrolladora senior, inspirada por el aprendizaje",
    "datos_estra": {
        "habilidades": "paciencia",
        "educacion": "universitaria",
        "certificacion": "good"
    }
}

new2 = {
    "id": "2",
    "nombre": "Sergio",
    "apellido": "Diaz",
    "username": "SergioD",
    "phone": 3116678233,
    "identificacion": 1054678189,
    "email": "sergiotoro@gmail.com",
    "password": "12345678",
    "pais": "Colombia",
    "ciudad": "Manizales",
    "direccion": "cll45c#12-38",
    "fech_nac": "23-04-2001",
    "fech_init": "10-02-2022",
    "descripcion": "Hola, estoy inspirado por la programacion",
    "datos_estra": {
        "habilidades": "perseverancia",
        "educacion": "maestria",
        "certificacion": "good"
    }
}


new3 = {
    "id": "2",
    "nombre": "Juan Diego",
    "apellido": "Agudelo",
    "username": "AgudeloJD",
    "phone": 3012334567,
    "identificacion": 10026778933,
    "email": "sergiotoro@gmail.com",
    "password": "amolavida",
    "pais": "Colombia",
    "ciudad": "Manizales",
    "direccion": "cll95c#10-87",
    "fech_nac": "06-11-1999",
    "fech_init": "20-04-2022",
    "descripcion": "Hola, amo mis estudios",
    "datos_estra": {
        "habilidades": "vocacion",
        "educacion": "maestria",
        "certificacion": "good"
    }
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