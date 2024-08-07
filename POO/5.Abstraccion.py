from abc import ABC, abstractmethod


class Personaje(ABC):

    @abstractmethod

    def __init__(self,nombre):

        self.nombre=nombre
        self.nivel=0
        self.inventario= []
        self.vida=100

    @abstractmethod

    def atacar(self,objetivo):

        pass

    @abstractmethod

    def getStatus(self):

        print(f"Nombre: {self.nombre}- Nivel: {self.nivel}")

    def subirDeNivel(self):

        self.nivel +=1

    def verInventario(self):

        print(f"Inventario de {self.nombre}")
        for objeto in self.inventario:
            print(objeto)


class Mago(Personaje):

    def __init__(self,nombre):

        super().__init__(nombre)
        self.vida=120
        self.inteligencia = 95
        self.inventario= ["pocion mana","Grimorio"]

    def getStatus(self):
        print(f"{self.nombre} es de la clase mago")
        super().getStatus()


    def atacar(self,objetivo):

        objetivo.vida -= self.inteligencia * 0.6
        print(f"El objetivo se ha quedado con {objetivo.vida}")

    def saludaer(self):
        print("Hola soy un mago")


class Guerrero(Personaje):

    def __init__(self,nombre):
        super().__init__(nombre)

        self.vida=200
        self.fuerza=75
        self.inventario=["Pocion de vida","Escudo","Espada"]

    def getStatus(self):
        
        print(f"{self.nombre} es de la clase Guerrero")
        super().getStatus()

    def atacar(self,objetivo):
        objetivo.vida -= self.fuerza * 0.8
        print(f"El objetivo se ha quedado con {objetivo.vida}")
        

mago1= Mago("juan")
guerrero1=Guerrero("Blackstar")

"""mago1.getStatus()
guerrero1.getStatus()

mago1.verInventario()
guerrero1.verInventario()"""

mago1.atacar(guerrero1)
guerrero1.atacar(mago1)