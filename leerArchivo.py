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
    diagnos=None
    a=1 #
    def parsear(self,ruta):
        if ruta:
            try:
                my_doc=ET.parse(ruta)
                self.raiz=my_doc.getroot()
                

                for pac in self.raiz.iter("paciente"):
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
                print(Fore.GREEN + "Archivo cargado con exito\n")
                return self.indice-1
            except:
                print(Fore.RED+ "Ocurrio un error al leer el achivo\n")
                
        
        
    def cargar(self,numero):
        if not self.segundoP:
            self.objeto=datosp.buscar(numero)
            self.m=self.objeto.tam
            self.lista = ListaDoble(self.m)
            self.periodos=ET.tostring(self.objeto.rej)
            almacenar.append(self.numero,self.periodos) #Agrego a la lista de periodos
            self.segundoP=True
            
        per=ET.fromstring(self.periodos)
        b=per.findall(".//celda")

        for i in range(1,self.m+1,1):
            for j in range(1,self.m+1,1):
                if len(b)!=0:
                    if i==int(b[0].attrib.get("f")) and j==int(b[0].attrib.get("c")):
                        self.lista.append(i,j,1)
                        b.pop(0)
                        continue
                self.lista.append(i,j)
        

    def nuevo_periodo(self): 
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
            self.lista.eliminarLista()
            

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
                if len(b)!=0:
                    if i==int(b[0].attrib.get("f")) and j==int(b[0].attrib.get("c")):
                            cadena+='<TD bgcolor="blue"></TD>\n'
                            b.pop(0)
                            continue
                cadena+="  <TD></TD>\n"
            cadena+=" </TR>\n"
        cadena+="</TABLE>>]"
    
        cadena+='}'
        Path(f"Persona{numero}").mkdir(exist_ok=True)
        file=open(f"./Persona{numero}/nodo.dot","w+")
        file.write(cadena)
        file.close()
        os.system(f"dot -Tpng ./Persona{numero}/nodo.dot -o ./Persona{numero}/periodo{self.numero}.png")


    def ejecutarAutom(self,numero):
        paso=True
        self.generarimg(numero)
        while self.numero<self.objeto.period and self.diagnos==None:
            if not paso:
                self.cargar(numero)
            self.nuevo_periodo()
            self.generarimg(numero)
            paso=False
        

    def reiniciar(self):
        self.segundoP=False
        self.indice=1
        self.numero=0
        self.diagnos=None
        almacenar.eliminar() #Elimina la lista que almacena los periodos
        
        