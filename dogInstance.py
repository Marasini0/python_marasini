#Class for Dog
class Dog:
    #class variable
    animal = 'dog'
    #the init method or constrructor
    def __init__(self, breed, color):
        #instance variable
        self.breed = breed
        self.color = color
        #objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
print("Rodger details:")
print("Rodger is a ", Rodger.animal)
print("Breed :", Rodger.breed)
print("Color :", Rodger.color)

print("\nBuzo Details:")
print("Buzo is a ", Buzo.animal)
print("Breed :", Buzo.breed)
print("Color :", Buzo.color)
