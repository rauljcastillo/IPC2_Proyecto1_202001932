import xml.etree.ElementTree as ET
from colorama import init,Fore
init(autoreset=True)

class Archivo:
    def cargar(self,ruta):
        try:
            my_doc=ET.parse(ruta)
            raiz=my_doc.getroot()
            print(Fore.GREEN+ "Archivo cargado con éxito\n")
        except:
            print(Fore.RED+ "Ocurrio un error al cargar el archivo\n")