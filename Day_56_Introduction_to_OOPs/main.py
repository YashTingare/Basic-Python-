# class Car:
#     a = 12 # Attributes

#     def hello():
#         print("Hello, I am Yash") # Method

# print(Car.a) # accessing the Attributes

# Car.hello() # Accessing the Method

# -------------------------------------------------------------------

 # Objects

# class Bags:
#     name = "Company"

#     def details(self):
#         print("Hello this is a company who manufature bags")

# reebok = Bags()  # This is Objects
# print(reebok.name)
# reebok.details()

#  -------------------------------------------------------------------

# Constructor

# class Bag:
#     def __init__(self, zips, material, pockets): # __init__ is constructor
#         self.zips = zips
#         self.material = material
#         self.pockets = pockets

# reebook = Bag(2, "Leather", 4)
# print(reebook.zips)
# print(reebook.material)
# print(reebook.pockets)

#  -------------------------------------------------------------------

# Type of Attributes & Methods

# class Aminal:
#     king = "lion" # Class Attributes

#     def __init__(self, name):
#         self.name = name # Instance/object Attributes

#     def hello(self): # Instance/object Method (Captures the location of object)
#         print(f"I will capture the loctaion of objects {self.name}")

#     @classmethod
#     def details(cls): # Class Methods captures the location of class
#         print(f"I will capture the location of classes {cls.king}")

#     @staticmethod
#     def greeting(): # this is static method it will not capture the location of class and object
#         print("Good morning")

#  -------------------------------------------------------------------

#INHERITANCE


## Single Inheritance 

# class Mainfactory:
     
#     def __init__(self,brand, material, zips, pockets):
#         self.brand = brand
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def details(self):
#         print(f"Requirement of {self.brand} Bag is: ")
#         print(f"Type of material is {self.material}")
#         print(f"No.of zip should be {self.zips}")
#         print(f"No.of pocket should be {self.pockets}")

# class Reebook(Mainfactory): #INHERITANCE
#     def __init__(self, material, zips, pockets, colour):
#         super().__init__("Reebook",material, zips, pockets)
#         self.colour = colour

#     def details(self):
#         super().details()
#         print(f"The colour of bag is {self.colour}")

# ## Multi level Inheritance
# class Nike(Mainfactory):
#     def __init__(self, material, zips, pockets, colour, hidepocket):
#         super().__init__("Nike",material, zips, pockets)
#         self.colour = colour
#         self.hidepocket = hidepocket
    
#     def details(self):
#         super().details()
#         print(f"The colour of bag is {self.colour}")
#         print(f"The No. of hidepocket is {self.hidepocket}")

# class Campus(Reebook):
#     def __init__(self, material, zips, pockets, colour, size):
#         super().__init__(material, zips, pockets, colour)
#         self.size = size
    
#     def details(self):
#         super().details()
#         print(f"The bag size should be {self.size}")

# reebook = Reebook("Leather", 3, 4, "Black")
# reebook.details()

# nike = Nike("polyster", 3,6,"Red",2)
# nike.details()

# campus = Campus("Plastic", 4, 6, "Gold", "60 liters")
# campus.details()

#  -------------------------------------------------------------------

# Multiple Inheritance

# class Animals:
#     def __init__(self, name):
#         self.name = name

# class Human:
#     def __init__(self, ID):
#         self.ID = ID

# class Robots(Animals, Human):
#     def __init__(self, name, ID):
#         Animals.__init__(self, name)
#         Human.__init__(self, ID)

# robo = Robots("Yash", 11)
# print(robo.name)
# print(robo.ID)

#  -------------------------------------------------------------------

# Polymorphism

# class Human:
#     def speak(self):
#         print("I am yash and i can speak")

# class Animals:
#     def speak(self):
#         print("I cant speak")


# obj1 = Human()
# obj1.speak()
# obj2 = Animals()
# obj2.speak()


# Method Overriding (we need Inheritance)

# class Animals:
#     a = 12
#     def __init__(self, name):
#         self.name = name

#     def details(self):
#         print(f"Your name is {self.name}")

# class Humans(Animals):
#     b = 13
#     def details(self):
#         print(f"Your info is {self.name}")

# obj = Humans("Yash")
# obj.details()

"""
When we are doing inheritance and parent and child
classes have same method name so the child class
method will override your parent class method.
"""

## Encapsulation hello

