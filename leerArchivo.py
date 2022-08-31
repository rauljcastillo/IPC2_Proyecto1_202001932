import xml.etree.ElementTree as ET
from ListaDoble import ListaDoble
from ListaAlmacenar import ListaAlmacenar
from datos import DatosP
from colorama import init,Fore

init(autoreset=True)
almacenar = ListaAlmacenar()
datosp=DatosP()

class Archivo:
    segundoP=False
    indice=1
    numero=0
    periods=0
    diagnos=0
    def parsear(self,ruta):
        if ruta:
            try:
                my_doc=ET.parse(ruta)
                self.raiz=my_doc.getroot()
                print(Fore.GREEN + "Archivo cargado con exito\n")
                cantidad=len(self.raiz.findall(".//datospersonales"))
                for elem in self.raiz.iter("datospersonales"):
                    datosp.agregar(self.indice,elem[0].text,elem[1].text)
                    self.indice+=1
                
                self.a=self.raiz.findall(".//periodos")
                self.tamanio=self.raiz.findall(".//m")
                self.rej=self.raiz.findall(".//rejilla")
                return cantidad
            except:
                print(Fore.RED+ "Ocurrio un error al leer el achivo\n")
                
        
        
    def cargar(self,numero):
        if not self.segundoP:
            self.m=int(self.tamanio[numero-1].text)
            self.lista = ListaDoble(self.m)
            self.periodos=ET.tostring(self.rej[numero-1])
            almacenar.append(self.periods,self.periodos)
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
        

    def nuevo_periodo(self,numero):
        
        if self.periods<int(self.a[numero-1].text):
            n = 0
            self.periods+=1
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
            self.diagnos=almacenar.append(self.periods,self.periodos)
            self.lista.eliminarLista()
        else:
            print(Fore.RED+"Ya se completaron los periodos")

    def reiniciar(self):
        self.segundoP=False
        self.indice=1
        self.numero=0
        datosp.eliminar() #ELimina la lista que tiene los nombres
        almacenar.eliminar() #Elimina la lista que almacena los periodos