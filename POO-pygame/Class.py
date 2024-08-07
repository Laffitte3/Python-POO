class Dog():

    """A class to represent a Dog"""

    def __init__(self, my_name,gender,age):

        """Initialize attributes"""
        self.name= my_name
        self.gender= gender
        self.age=age

    def eat(self):
        """Feed the dog"""

        if self.gender == "male":

            print(f"Here {self.name} Good boy, puedes comer")
        else:
            print(f"Here {self.name} Good girl, puedes comer")

    def bark(self,is_loud):
        """Get the dog to speak"""

        if is_loud == True:
            print("WOOF WOOF WOOF WOOF")
        else:
            print("woof...")

    def compute_age(self):

        calculo_edad= self.age * 7
        print(f"{self.name} tiene {calculo_edad}")
        return calculo_edad

    def is_alive(self,status):

        edad=self.compute_age()

        if status== True:
            print(f"Yes, is still alive and has {edad}")

        else: 
            print(f"No {self.name} is not alive")


#Create 2 dog objects
dog1=Dog("Kenny","male",9)
dog2=Dog("Penelope","female",1)

#dog1.compute_age()
#dog2.compute_age()

dog1.is_alive(True)