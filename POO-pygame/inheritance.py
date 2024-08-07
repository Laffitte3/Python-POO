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

        
        if status== True:
            edad=self.compute_age()
            print(f"Yes, is still alive and has {edad}")

        else: 
            print(f"No {self.name} is not alive")

class Beagle(Dog):

    """A class to represent an specific dog"""
    def __init__(self,my_name,gender,age,is_gun_shy):
        
        #Call the initialization method of the parent(super) class
        super().__init__(my_name,gender,age)

        self.is_gun_shy= is_gun_shy

    def hunt(self):
        """if the dog is not gun shy, take them hunting"""

        if not self.is_gun_shy:

            self.bark(True)
            print(f"{self.name} lets go, bring me a duck")

        else:

            print(f"{self.name} is not a good hunting dog")
    
    #Modificamos el metodo Bark para la clase Beagle

    def bark(self,is_loud):

        if is_loud == True:

            print("Howl Howl HowLLLLLLL")

        else:
            print("Howl")

class Rotwailer(Dog):

    def __init__(self,my_name,gender,age,is_house_alone,angry,bite):

        super().__init__(my_name,gender,age)

        self.is_house_alone = is_house_alone
        self.angry= angry
        self.bite=bite


    def protect(self):

        if self.is_house_alone:

            print("Protect the house")

        else: 
            print(f"We can go to the park {self.name}")

    def bark(self,is_loud):

        if is_loud == True and self.angry== True:
            print("WOOF WOOF WOOF WOOF")

        elif is_loud == True and self.angry== False:
            print("woof woof woof")

        else:
            print("woof...")


    def molesto(self):

        if self.angry == True:
            ataque=40
        else:
            ataque=10

        mordida= self.bite * ataque

        print(f"Muy bien {self.name} hiciste {mordida} de dano")

rottwailer=Rotwailer("Rotty","male",4,False,False,50)

rottwailer.eat()
rottwailer.bark(True)
rottwailer.bark(False)
rottwailer.is_alive(True)
rottwailer.molesto()