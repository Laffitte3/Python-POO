class Celular():

    variable_ejemplo = "Ejemplo"

    def __init__(self, color):
        
        self.color= color

    def encender(self,contrasena):

        print(f"Encendiendo telefono: {contrasena}")
        print(self.color)

    def apagado(self):

        print("Apagando Telefono")


objeto_celular = Celular("blanco")
print(objeto_celular.color)
objeto_celular.encender(242321)