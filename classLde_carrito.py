from clientes import productos

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

producto1 = productos[0]
producto2 = productos[1]
producto3 = productos[2]

# agregar mi primer produto al carrito
lista.insertar_a_listaVacia(producto2)

# agregar otro producto al carrtio

lista.insertar_despues_del_elemento(producto2, producto1)

# agregar otro producto al carrito 
lista.insertar_despues_del_elemento(producto1, producto3)

lista.atravezar_lista()

# eliminar producto de la lista
print("--------------------------------------------------------------------")
print("Producto eliminado")
print("--------------------------------------------------------------------")

lista.eliminar_un_elemento_dado(producto2)
lista.atravezar_lista()
