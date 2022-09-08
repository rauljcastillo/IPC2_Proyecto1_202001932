import xml.etree.ElementTree as ET
from ListaDoble import ListaDoble
from ListaAlmacenar import ListaAlmacenar
from datos import DatosP
from Listasalida import Listasalida
from colorama import init,Fore
import os
from pathlib import Path

init(autoreset=True)
almacenar = ListaAlmacenar()
datosp=DatosP()
listasal=Listasalida()

class Archivo:
    
    segundoP=False
    indice=1 #indice de cada nodo
    numero=0 #Indica en que periodo vamos
    diagnos=None #Almacena el numero de diagnostico si se repite un periodo de lo contrario, almacena None
    a=1 #
    def parsear(self,ruta):
        if ruta:
            try:
                my_doc=ET.parse(ruta)  #Parseo la ruta
                self.raiz=my_doc.getroot()
                print(Fore.GREEN + "Archivo cargado con exito\n")

                for pac in self.raiz.iter("paciente"): #Almaceno en la Lista datos todos las caracteristicas de un paciente
                    datos=pac.find(".//datospersonales")
                    perio=pac.find(".//periodos")
                    m=pac.find(".//m")
                    rej=pac.find(".//rejilla")
                    datosp.agregar(self.indice,datos[0].text,datos[1].text,int(perio.text),int(m.text),rej)
                    self.indice+=1
                datos=None
                perio=None
                m=None
                rej=None

                return self.indice-1 #Retorno la cantidad de pacientes en el archivo
            except:
                print(Fore.RED+ "Ocurrio un error al leer el achivo\n")
                
        
        
    def cargar(self,numero):
        if not self.segundoP: #Devuelve los datos de un paciente
            self.objeto=datosp.buscar(numero)
            self.m=self.objeto.tam
            self.lista = ListaDoble(self.m)
            self.periodos="<rejilla>\n"
            for elem in self.objeto.rej.iter("celda"):
                self.periodos+=f'<celda f="{elem.attrib["f"]}" c="{elem.attrib["c"]}" />\n'
            self.periodos+="</rejilla>\n"

            almacenar.append(self.numero,self.periodos) #Agrego a la lista de periodos
            self.segundoP=True
                
        per=ET.fromstring(self.periodos) #Parseo de los periodos
        b=per.findall(".//celda") #Devuevel todas las celdas de un paciente

        for i in range(1,self.m+1,1):   #Carga a la lista principal las celdas contagiadas y no contagiadas
            for j in range(1,self.m+1,1):
                if (f"{i}",f"{j}") in ((x.attrib.get("f"),x.attrib.get("c")) for x in b):
                    self.lista.append(i,j,1)
                    continue
                self.lista.append(i,j)
        b=None
        

    def nuevo_periodo(self): #Ejecuta un nuevo periodo
        if self.numero<self.objeto.period and self.diagnos==None:
            n = 0
            self.numero+=1
            self.periodos = "<rejilla>\n"
            for i in range(1, self.m+1, 1):
                for j in range(1, self.m+1, 1):
                    if j == 1:
                        var1 = self.lista.buscar(i, j)
                        if var1.cont == 0:
                            if var1.siguiente.cont == 1:
                                n += 1
                            var2 = self.lista.buscar(i-1, j)
                            if var2:
                                if var2.cont == 1:
                                    n += 1
                                if var2.siguiente.cont == 1:
                                    n += 1
                            var3 = self.lista.buscar(i+1, j)
                            if var3:
                                if var3.cont == 1:
                                    n += 1
                                if var3.siguiente.cont == 1:
                                    n += 1
                            if n == 3:
                                self.periodos += f'<celda f="{i}" c="{j}" />\n'
                                n = 0
                                continue

                            n = 0
                            continue
                        if var1.cont == 1:
                            if var1.siguiente.cont == 1:
                                n += 1
                            var2 = self.lista.buscar(i-1, j)
                            if var2:
                                if var2.cont == 1:
                                    n += 1
                                
                                if var2.siguiente.cont == 1:
                                    n += 1

                            var3 = self.lista.buscar(i+1, j)
                            if var3:
                                if var3.cont == 1:
                                    n += 1

                                

                                if var3.siguiente.cont == 1:
                                    n += 1

                            if n == 2 or n==3:
                                self.periodos += f'<celda f="{i}" c="{j}" />\n'
                                n = 0
                                continue

                            n = 0
                            continue
                    if j == self.m:
                        var1 = self.lista.buscar(i, j)
                        if var1.cont == 0:
                            if var1.anterior.cont == 1:
                                n += 1
                            var2 = self.lista.buscar(i-1, j)
                            if var2:
                                if var2.cont == 1:
                                    n += 1
                                if var2.anterior.cont == 1:
                                    n += 1
                            var3 = self.lista.buscar(i+1, j)
                            if var3:
                                if var3.cont == 1:
                                    n += 1
                                if var3.anterior.cont == 1:
                                    n += 1
                            if n == 3:
                                self.periodos += f'<celda f="{i}" c="{j}" />\n'
                                n = 0
                                continue

                            n = 0
                            continue
                        if var1.cont == 1:
                            if var1.anterior.cont == 1:
                                n += 1

                            var2 = self.lista.buscar(i-1, j)
                            if var2:
                                if var2.cont == 1:
                                    n += 1
                        
                                if var2.anterior.cont == 1:
                                    n += 1

                            var3 = self.lista.buscar(i+1, j)
                            if var3:
                                if var3.cont == 1:
                                    n += 1

                                if var3.anterior.cont == 1:
                                    n += 1

                            if n == 2 or n==3:
                                self.periodos += f'<celda f="{i}" c="{j}" />\n'
                                n = 0
                                continue

                            n = 0
                            continue
                    else:
                        var1 = self.lista.buscar(i, j)
                        if var1.cont == 0:
                            if var1.siguiente.cont == 1:
                                n += 1
                            if var1.anterior.cont == 1:
                                n += 1
                            var2 = self.lista.buscar(i-1, j)
                            if var2:
                                if var2.cont == 1:
                                    n += 1
                                if var2.siguiente.cont == 1:
                                    n += 1

                                if var2.anterior.cont == 1:
                                    n += 1
                            var3 = self.lista.buscar(i+1, j)
                            if var3:
                                if var3.cont == 1:
                                    n += 1

                                if var3.siguiente.cont == 1:
                                    n += 1

                                if var3.anterior.cont == 1:
                                    n += 1
                            if n == 3:
                                self.periodos += f'<celda f="{i}" c="{j}" />\n'
                                n = 0
                                continue

                            n = 0
                            continue
                        if var1.cont == 1:
                            if var1.siguiente.cont == 1:
                                n += 1
                            if var1.anterior.cont == 1:
                                n += 1
                            var2 = self.lista.buscar(i-1, j)
                            if var2:
                                if var2.cont == 1:
                                    n += 1
                                if var2.siguiente.cont == 1:
                                    n += 1

                                if var2.anterior.cont == 1:
                                    n += 1

                            var3 = self.lista.buscar(i+1, j)
                            if var3:
                                if var3.cont == 1:
                                    n += 1

                                if var3.siguiente.cont == 1:
                                    n += 1

                                if var3.anterior.cont == 1:
                                    n += 1
                            if n == 2 or n==3:
                                self.periodos += f'<celda f="{i}" c="{j}" />\n'
                                n = 0
                                continue

                            n = 0
                            continue
            self.periodos += "</rejilla>\n"
            self.diagnos=almacenar.append(self.numero,self.periodos) #Almacena en la lista de periodos
            self.lista.eliminarLista() #Elimino lo que halla en la lista principal 
            

    def generarimg(self,numero):
        per=ET.fromstring(self.periodos)
        b=per.findall(".//celda")
        cadena='digraph { '
        cadena+=f'label="Periodo {self.numero}"'
        cadena+='node [shape=none]'
        cadena+="n1 [label =\n"
        cadena+='<<TABLE border="2" cellspacing="3" cellpadding="10" bgcolor="white">'

        for i in range(1,self.m+1,1):
            cadena+=" <TR>\n"
            for j in range(1,self.m+1,1):
                if (f"{i}",f"{j}") in ((x.attrib.get("f"),x.attrib.get("c")) for x in b):
                    cadena+='<TD bgcolor="blue"></TD>\n'    
                    continue
                cadena+="  <TD></TD>\n"
            cadena+=" </TR>\n"
        cadena+="</TABLE>>]"
    
        cadena+='}'
        b=None
        Path(f"Persona{numero}").mkdir(exist_ok=True) #Pregunta si ya existe una carpeta sino la crea
        file=open(f"./Persona{numero}/nodo.dot","w+") #Escribo un archivo dot
        file.write(cadena) 
        file.close()
        os.system(f"dot -Tpng ./Persona{numero}/nodo.dot -o ./Persona{numero}/periodo{self.numero}.png")


    def ejecutarAutom(self,numero): #Ejecuta periodos automaticos
        paso=True
        #self.generarimg(numero)
        while self.numero<self.objeto.period and self.diagnos==None:
            if not paso:     #La primera vez no pasará por aqui
                self.cargar(numero)
            self.nuevo_periodo()
            #self.generarimg(numero)
            paso=False
        

    def reiniciar(self): #Reinicia todas las variables a sus valores iniciales
        self.segundoP=False
        self.indice=1
        self.numero=0
        self.diagnos=None
        almacenar.eliminar() #Elimina la lista que almacena los periodos
        
    def diagnostico(self):    #Almacena en la listaSalida los resultados para cada paciente
        
        if self.diagnos is None:
            listasal.agregar(self.a,self.objeto.nombre,self.objeto.edad,self.objeto.period,self.objeto.tam,"Leve",self.numero,0)
            self.a+=1
            return 
        if self.diagnos == 2:
            listasal.agregar(self.a,self.objeto.nombre,self.objeto.edad,self.objeto.period,self.objeto.tam,"Grave",self.numero,self.diagnos)
            self.a+=1
            return
        if self.diagnos > 2:
            listasal.agregar(self.a,self.objeto.nombre,self.objeto.edad,self.objeto.period,self.objeto.tam,"Grave",self.numero,self.diagnos)
            self.a+=1
            return 
        if self.diagnos ==1:
            listasal.agregar(self.a,self.objeto.nombre,self.objeto.edad,self.objeto.period,self.objeto.tam,"Mortal",self.numero,0)
            self.a+=1
            return 
    
    
    def crearArchivo(self):
        archivo="<pacientes>\n"
        tam=listasal.tamaniolista()
        for el in range(1,tam+1,1):
            archivo+="    <paciente>\n"
            pc=listasal.buscar(el)
            archivo+="        <datospersonales>\n"
            archivo+=f"            <nombre>{pc.nombre}</nombre>\n"
            archivo+=f"            <edad>{pc.edad}</edad>\n"
            archivo+="        </datospersonales>\n"
            archivo+=f"       <periodos>{pc.periodos}</periodos>\n"
            archivo+=f"       <m>{pc.m}</m>\n"
            archivo+=f"       <resultado>{pc.resultado}</resultado>\n"
            archivo+=f"       <n>{pc.n}</n>\n"
            archivo+=f"       <n1>{pc.n1}</n1>\n"
            archivo+="    </paciente>\n"

        archivo+="</pacientes>"

        file=open("./Diagnosticos.xml","w+",encoding="utf-8")
        file.write(archivo)
        file.close()
        
        