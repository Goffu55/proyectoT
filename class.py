class categorias: 
    nameCategorias = ["diseño", "programacion", "educacion"]
    durabilidadMeses = [5, 7, 2]

def quicksort(durabilidadMeses):
    if not durabilidadMeses:
        return []
    return (quicksort([x for x in durabilidadMeses[1:] if x <  durabilidadMeses[0]])
            + [durabilidadMeses[0]] +
            quicksort([x for x in durabilidadMeses[1:] if x >= durabilidadMeses[0]]))

print(quicksort(categorias.durabilidadMeses))

palabra = "diseño"
def search(palabra):
    i = 0
    listaB = []
    while i < len(categorias.nameCategorias):
        busqueda = palabra in categorias.nameCategorias
        listaB.append(busqueda)
        
        if (busqueda == True):
            print("Palabra: " + categorias.nameCategorias[i])
            print()
            i += 1    
        else:
            i += 1
    if(listaB.count(True) == 0):
        print(f'la palabra "{palabra}" no fue encontrada')
print(search(palabra))

class carrito: 
    serviciosIngresados = ["Html, CSS, JavaScript", "POO", "Licenciatura en enseñanza"]
    cursosInscritos = [3, 10, 12]

def quicksort(cursosInscritos):
    if not cursosInscritos:
        return []
    return (quicksort([x for x in cursosInscritos[1:] if x <  cursosInscritos[0]])
            + [cursosInscritos[0]] +
            quicksort([x for x in cursosInscritos[1:] if x >= cursosInscritos[0]]))

print(quicksort(carrito.cursosInscritos))

palabra2 = "POO"
def search(palabra):
    i = 0
    listaB = []
    while i < len(carrito.serviciosIngresados):
        busqueda = palabra in carrito.serviciosIngresados
        listaB.append(busqueda)
        
        if (busqueda == True):
            print("Palabra: " + carrito.serviciosIngresados[i])
            print()
            i += 1    
        else:
            i += 1
    if(listaB.count(True) == 0):
        print(f'la palabra "{palabra}" no fue encontrada')
print(search(palabra2))

def search(palabra):
    i = 0
    listaB = []
    while i < len(categorias.nameCategorias):
        busqueda = palabra in categorias.nameCategorias
        listaB.append(busqueda)
        
        if (busqueda == True):
            print("Palabra: " + categorias.nameCategorias[i])
            print()
            i += 1    
        else:
            i += 1
    if(listaB.count(True) == 0):
        print(f'la palabra "{palabra}" no fue encontrada')
print(search(palabra))

class membresias: 
    tipoMembresia = ["basic", "estandar", "premium"]
    price = [50.00, 85.00, 190.00]

def quicksort(price):
    if not price:
        return []
    return (quicksort([x for x in price[1:] if x <  price[0]])
            + [price[0]] +
            quicksort([x for x in price[1:] if x >= price[0]]))

print(quicksort(membresias.price))

palabra3 = "basic"
def search(palabra):
    i = 0
    listaB = []
    while i < len(membresias.tipoMembresia):
        busqueda = palabra in membresias.tipoMembresia
        listaB.append(busqueda)
        
        if (busqueda == True):
            print("Palabra: " + membresias.tipoMembresia[i])
            print()
            i += 1    
        else:
            i += 1
    if(listaB.count(True) == 0):
        print(f'la palabra "{palabra}" no fue encontrada')
print(search(palabra3))