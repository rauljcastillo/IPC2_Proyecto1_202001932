class Nodo:
    def __init__(self,indice,nombre,edad,period,tam,rejilla):
        self.indice=indice
        self.nombre=nombre
        self.edad=edad
        self.period=period
        self.tam=tam
        self.rej=rejilla 
        self.siguiente=None

class DatosP:
    def __init__(self):
        self.primero=None

    def agregar(self,indice,nombre,edad,period,tam,rejilla):
        if self.primero is None:
            self.primero=Nodo(indice,nombre,edad,period,tam,rejilla)
            return
        actual=self.primero
        while actual.siguiente != None:
            actual=actual.siguiente
        actual.siguiente=Nodo(indice,nombre,edad,period,tam,rejilla)

    def eliminar(self):
        self.primero=None
    
    def buscar(self,numero):
        actual=self.primero
        while actual!=None:
            if actual.indice==numero:
                return actual
            actual=actual.siguiente
