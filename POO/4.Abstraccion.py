
from abc import ABC, abstractmethod


class Celular(ABC):

    @abstractmethod

    def __init__(self,color,almacenamiento):

        self.color = color
        self.almacenamiento=almacenamiento

    def informacion(self):

        print(f" Color: {self.color}")
        print(f"Almacenamiento: {self.almacenamiento}Gb")

    def encender(self):

        print("Encendiendo celular")

    def apagar(self):

        print("Apagando celular")

class Android(Celular):

    def __init__(self, color,almacenamiento):
        
        super(Android,self).__init__(color,almacenamiento)
    

    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento")


class Iphone(Celular):

    def transferir_archivo(self):
        print("Transfiriendo archivos")


#objeto=Celular("blanco",128)
celular_android=Android("rojo",128)