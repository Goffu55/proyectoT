from classCategorias import categorias
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
print(search(palabra2))