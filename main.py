from leerArchivo import Archivo
archivo=Archivo()

def main():
    opc=""
    while opc!= '2':
        print("*****Menu*****")
        print("1.Cargar archivo")
        print("2.Salir")
        opc=input("Ingrese una opcion: \n")
        if opc=="1":
            cargararchivo()

def cargararchivo():
    opcion=""
    var=""
    ruta=input("\nIngrese ruta del archivo:\n")
    cantidad=archivo.parsear(ruta)
    if cantidad:
        for i in range(1,cantidad+1,1):
            var+=f"{i}.Persona {i}\n"
        var+=f"{cantidad+1}.Salir"

        while opcion != f"{cantidad+1}":
            print(var)
            opcion=input("Ingresa un opción:\n")
            if opcion=="1":
                tercermenu(1)
            if opcion=="2":
                tercermenu(2)
            if opcion==f"{cantidad+1}":
                archivo.reiniciar()


def tercermenu(numero):
    op=""
    while op!="4":
        print("1.Ejecutar Periodo")
        print("2.Ver patrón")
        print("3.Diagnostico")
        print("4.Salir")
        op=input("Ingrese opcion: \n")
        if op=="1":
            archivo.cargar(numero)
            archivo.nuevo_periodo(numero)
        if op=="2":
            archivo.cargar(numero)
            
        if op=="3":
            print("#")
        if op=="4":
            archivo.reiniciar()

main()