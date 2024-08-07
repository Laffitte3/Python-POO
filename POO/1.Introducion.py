

class Celular():

    def __init__(self, color,marca):

        self.color = color
        self.marca = marca

    def encender(self):

        print("Encendiendo celular")

    def apagar(self):

        print("Apagandpo celular")
    
    def datos_del_celular(self):
        print(f"color: {self.color}, marca: {self.marca}")


celular1=Celular("rojo","samsung")

celular1.datos_del_celular()

celular2=Celular("Azul","Pixel")

celular2.datos_del_celular()

celular2.encender()
celular2.apagar()


