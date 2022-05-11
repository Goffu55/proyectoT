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