
from abc import ABC, abstractmethod


class Celular(ABC):

    @abstractmethod

    def __init__(self,color,almacenamiento):

        self.color = color
        self.almacenamiento=almacenamiento

    def informacion(self):

        print(f" Color: {self.color}")
        print(f"Almacenamiento: {self.almacenamiento}Gb")

    @abstractmethod

    def encender(self):

        print("Encendiendo celular")

    def apagar(self):

        print("Apagando celular")

class Android(Celular):

    def __init__(self, color,almacenamiento):
        
        super().__init__(color,almacenamiento)
    

    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento")


    def encender(self):

        print("Mostrando logo de Android")


class Iphone(Celular):

    def __init__(self, color,almacenamiento):
        
        super().__init__(color,almacenamiento)

    def transferir_archivo(self):
        super().encender()
        print("Transfiriendo archivos")

    def encender(self):
        super().encender()
        print("Mostrando logo de Iphone")


iphone12=Iphone("black",128)

iphone12.encender()

