from clientes import usuarios
class ldeUsers:

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

