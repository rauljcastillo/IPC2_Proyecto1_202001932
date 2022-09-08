class Nodo:
    def __init__(self,num_per,dato,siguiente=None):
        self.numper=num_per
        self.dato=dato
        self.siguiente=siguiente

class ListaAlmacenar:
    repetido=False
    def __init__(self):
        self.primero=None
    
    def append(self,numper,period):
        if self.primero is None:
            self.primero=Nodo(numper,period)
            return
        
        actual=self.primero
        while actual.siguiente != None and actual.dato!=period:
            actual=actual.siguiente
        if actual.dato==period:
            print("El periodo ya existe")
            return numper-actual.numper
        actual.siguiente=Nodo(numper,period)

    def print(self):
        actual=self.primero
        while actual != None:
            print(actual.dato)
            actual=actual.siguiente
            
    def eliminar(self):
        self.primero=None