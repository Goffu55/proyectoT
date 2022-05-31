from clientes import extra

class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None

class listaDoblementeEnlazada:
    def __init__(self):
        self.start_node = None
    
    def insertar_a_listaVacia(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("la lista no está vicía")

    def insertar_despues_del_elemento(self, x, data):
        if self.start_node is None:
            print("la lista está vacía")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("el elemento no está en la lista")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def insertar_antes_del_elemento(self, x, data):
        if self.start_node is None:
            print("la lista está vacía")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("el elemento no está en la lista")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def atravezar_lista(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.nref
    
    def eliminar_un_elemento_dado(self, x):
        if self.start_node is None:
            print("Esta lista no tiene elementos para eliminar")
            return 
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("elemento no encontrado")
            return 

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

lista = listaDoblementeEnlazada()

prueba = { "id": "4", "nombre": "Ginna", "apellido": "Tangarife", "datos_estra": {
        "habilidades": "Python",
        "educacion": "Superior",
        "certificacion": "Certificada",
    }
}
prueba2 = {"id": "5", "nombre": "Sergio", "apellido": "Diaz", "datos_estra": {
        "habilidades": "HTML",
        "educacion": "Media",
        "certificacion": "Certificado",
    },
}
i = 0

while i < len(extra):
    if i == 0:
        lista.insertar_a_listaVacia(extra[i])
        i += 1
    else: 
        lista.insertar_despues_del_elemento(extra[i-1],extra[i])
        i += 1

# lista.insertar_despues_del_elemento("11","12")

lista.atravezar_lista()
print("---------------------------------------------------------------")


lista.insertar_antes_del_elemento(extra[1], prueba2)

lista.atravezar_lista()


lista.eliminar_un_elemento_dado(prueba2)
print("---------------------------------------------------------------")
lista.atravezar_lista()