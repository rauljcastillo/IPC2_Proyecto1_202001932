class Nodo:
    def __init__(self,nombre,edad,indice):
        self.indice=indice
        self.nombre=nombre
        self.edad=edad 
        self.siguiente=None

class DatosP:
    def __init__(self):
        self.primero=None
    def agregar(self,indice,nombre,edad):
        if self.primero is None:
            self.primero=Nodo(indice,nombre,edad)
            return
        actual=self.primero
        while actual.siguiente != None:
            actual=actual.siguiente
        actual.siguiente=Nodo(indice,nombre,edad)

    def print(self):
        actual=self.primero
        while actual != None:
            print(actual.nombre, end=" => ")
            actual=actual.siguiente
    def eliminar(self):
        self.primero=None