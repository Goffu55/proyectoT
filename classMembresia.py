class membresias: 

    tipoMembresia = ["basic", "estandar", "premium"]
    price = [50.00, 85.00, 190.00]

# Ordenamos la lista de datos

def quicksort(price):
    if not price:
        return []
    return (quicksort([x for x in price[1:] if x <  price[0]])
            + [price[0]] +
            quicksort([x for x in price[1:] if x >= price[0]]))

print(quicksort(membresias.price))

# Se Busca la palabra si existe dentro de la lista

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

    