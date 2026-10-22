class Animal: # This is the parent class that creates name attribute and the common methods to be used by it's child classes.
    def __init__(self, name: str):
        self.name = name
# I create the common methods which is eat and make_sound.
    def eat(self):
        print(f"{self.name} is eating.") 
# This is the base generic method
    def make_sound(self):
        print(f"{self.name} is making a sound.")

class Lion(Animal): # The first of 3 classes which is Lion 
    def __init__(self, name: str):
        super().__init__(name) # We iniatialize it and we use the super() function to inherit name attribute.
    
    def eat(self):
        print(f"{self.name} is eating fresh meat.") 
# This part we utilize method ovveride where instead of using the generic 'is eating' it has is eating fresh meat.
    def make_sound(self):
        print(f"{self.name} roars loudly!")
# And vice versa for make_sound it has roars loudly! rather than is making a sound.

class Elephant(Animal):
    def __init__(self, name: str):
        super().__init__(name)
# It is the same here for Lion it both inherits name attribute and
    def eat(self):
        print(f"{self.name} grass and fruits")
# overrides both eat and make_sound with its own special unique message like 'grass and fruits' and 'thrumpets'
    def make_sound(self):
        print(f"{self.name} thrumpets")
# Another thing is that it takes the same methods and attributtes but changes it.

class Monkey(Animal):
    def __init__(self, name: str):
        super().__init__(name)
    # for the Monkey child class it follows the same processes as the prior cchild classes. It inherits name through super() and modifies the methods. 
    def eat(self):
        print(f"{self.name} banana's")
    # Thw method alkso goes through method override each having it's own unique messages.
    def make_sound(self):
        print(f"{self.name} chatters")

Simba = Lion("Simba")
Dumbo = Elephant("Dumbo") # This initialize objects with the only attribute being name.  
George = Monkey("George") # But it represent each child class with appropriate naming.

animals = [Simba, Dumbo, George] # I created a list so I don't need to type each object with its method.
print(f"\n")
for i in animals:
    i.make_sound() # This for loop is created so it prints all the actions like make_sound and eat without me typing everything.
    i.eat()
    print(f"\n") 

