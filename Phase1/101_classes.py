

class Dog:
    def __init__(self , name: str , age : int): # Constructor with type hints
        self.name = name
        self.age = age

    def bark(self) -> None: # Method with return type hint
        print(self.name + " says Woof!")
        
        
my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Buddy says Woof!    




# Instance vs Class Variables
# Instance variables are unique to each instance of a class, while class variables are shared among all instances of the class.
class Cat:
    species = "Felis catus"  # Class variable

    def __init__(self, name: str, age: int):
        self.name = name      # Instance variable
        self.age = age        # Instance variable

my_cat1 = Cat("Whiskers", 2)
my_cat2 = Cat("Tom", 5)


print(my_cat1.species)  # Output: Felis catus
print(my_cat2.species)  # Output: Felis catus