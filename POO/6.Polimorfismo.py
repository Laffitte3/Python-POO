class Empleados():

    def __init__(self,nombre,sueldoMensual):
        
        self.nombre=nombre
        self.sueldoMensual=sueldoMensual

    def calcularSueldoAnual(self):

        sueldoAnual=self.sueldoMensual*12 *(1 +1/100)
        print(f"El sueldo de {self.nombre} es de {sueldoAnual}$")


class Contable(Empleados):

    def __init__(self,nombre,sueldoMensual):

        super().__init__(nombre,sueldoMensual)

    
    def calcularSueldoAnual(self):
        sueldoAnual=self.sueldoMensual*12 *(1 +4/100)
        print(f"El sueldo de {self.nombre}, contable es de {sueldoAnual}$")

class Publicista(Empleados):

    def __init__(self,nombre,sueldoMensual):

        super().__init__(nombre,sueldoMensual)

    def calcularSueldoAnual(self):
        
        sueldoAnual=self.sueldoMensual*12 *(1 +5/100)
        print(f"El sueldo de {self.nombre}, Publicista es de {sueldoAnual}$")

class Becario(Empleados):


    def calcularSueldoAnual(self):
        
        sueldoAnual=self.sueldoMensual*12 
        print(f"El sueldo de {self.nombre}, Becario es de {sueldoAnual}$")




empleados=[
    Empleados("Juan",1000),
    Publicista("Angela",1300),
    Contable("Jenifer",1200),
    Becario("Angel",800)

]


for empleado in empleados:

    empleado.calcularSueldoAnual()

