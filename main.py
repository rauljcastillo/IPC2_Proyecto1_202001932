from leerArchivo import Archivo
archivo=Archivo()
paso=False
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
        var+=f"{cantidad+1}.Archivo Diagnosticos\n"
        var+=f"{cantidad+2}.Salir"

        while opcion != cantidad+2:
            print(var)
            opcion=int(input("Ingresa un opción:\n"))
            if opcion==1 or opcion<=cantidad:
                tercermenu(opcion)




def tercermenu(numero):
    op=""
    global paso
    while op!="4":
        print("1.Ejecutar periodos automaticos")
        print("2.Ejecutar periodo por periodo")
        print("3.Ver patrón")
        print("4.Salir")
        op=input("Ingrese opcion: \n")

        if op=="1":
            archivo.cargar(numero)
            archivo.ejecutarAutom(numero)

        if op=="2":
            archivo.cargar(numero)
            archivo.nuevo_periodo()

        if op=="3":
            if not paso:
                archivo.cargar(numero)
                paso=True
            archivo.generarimg(numero)
        if op=="4":
            archivo.reiniciar()
            paso=False

main()