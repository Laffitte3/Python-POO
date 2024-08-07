
#Clase padre
class Celular():

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

    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento")


class Iphone(Celular):

    def transferir_archivo(self):
        print("Transfiriendo archivos")


celular_android=Android("blanco",128)
celular_android.expandir_almacenamiento()
celular_android.informacion()

celular_iphone=Iphone("Violeta",64)
celular_iphone.transferir_archivo()
