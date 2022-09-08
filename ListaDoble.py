class Nodo:
    def __init__(self,fil,col,cont=0, anterior=None, siguiente=None):
        self.fil=fil
        self.col=col
        self.cont=cont
        self.anterior = anterior
        self.siguiente = siguiente


class ListaDoble: #Esta es la lista principal donde se cargaran las celulas contagiadas
    def __init__(self,tamanio):
        self.cabeza = None
        self.tamanio=tamanio

    def append(self,fil,col,cont=0):
        if self.cabeza is None:
            self.cabeza = Nodo(fil,col,cont)
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        nuevo_nodo = Nodo(fil,col,cont)
        actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = actual

    def buscar(self,fil,col):
        if (col<1 or col>self.tamanio) or(fil<1 or fil>self.tamanio):
            return
        actual=self.cabeza
        while actual != None:
            if actual.fil==fil and actual.col==col:
                return actual
            actual=actual.siguiente

    def eliminarLista(self):
        self.cabeza= None