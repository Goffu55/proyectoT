class ProductFind:
    
    def search(palabra):
        i = 0
        j = 0
        listaB = []
        while i < len(usuarios):
           
            if len(usuarios[i]['productos']) > 0:
                busqueda = palabra in usuarios[i]['productos'][j]["nombre_product"]
                listaB.append(busqueda)
                
                if (busqueda == True):
                    print("id: " + usuarios[i]['productos'][i]['id'])
                    print("nombre product: " + usuarios[i]['productos'][i]['nombre_product'])
                    print("descripcion product: " + usuarios[i]['productos'][i]['descripcion_product'])
                    print("categoria: " + usuarios[i]['productos'][i]['categoria'])
                    print("precio: " + usuarios[i]['productos'][i]['price'])
                    i += 1
                    break
                else:
                    j += 1
            if(listaB.count(True) == 0):
                print(f'la palabra "{palabra}" no fue encontrada')

palabra = "miguelon3,0"
print(ProductFind.search(palabra))