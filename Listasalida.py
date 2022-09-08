class Nodo:
    def __init__(self,num,nombre,edad,periodos,m,resultado,n,n1):
        self.num=num
        self.nombre=nombre
        self.edad=edad
        self.periodos=periodos
        self.m=m
        self.resultado=resultado
        self.n=n
        self.n1=n1
        self.siguiente=None
        
class Listasalida: #Esta lista almacena el diagnostico de un paciente
    cantidad=0
    def __init__(self) -> None:
        self.primero=None
    
    def agregar(self,num,nombre,edad,periodos,m,resultado,n,n1):
        self.cantidad+=1
        if self.primero is None:
            self.primero=Nodo(num,nombre,edad,periodos,m,resultado,n,n1)
            return 
        actual=self.primero
        while actual.siguiente != None:
            actual=actual.siguiente
        actual.siguiente=Nodo(num,nombre,edad,periodos,m,resultado,n,n1)
    
    def tamaniolista(self):
        return self.cantidad
    
    def buscar(self,numero):
        actual=self.primero
        while actual!=None:
            if actual.num == numero:
                return actual
            actual=actual.siguiente