from leerArchivo import Archivo
inst=Archivo()
def menu():

    
    opc=""

    while opc!='2':
        print("****Menu****")
        print("1.Cargar archivo")
        print("2.Salir")
        opc=input("Ingrese opción: \n")
        if opc=="1":
            ingresar()
            


def ingresar():
    ruta=input("Ingrese ruta del archivo\n")
    inst.cargar(ruta)


menu()
