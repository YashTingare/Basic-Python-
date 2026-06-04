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

class Mainfactory:
     
    def __init__(self,brand, material, zips, pockets):
        self.brand = brand
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def details(self):
        print(f"Requirement of {self.brand} Bag is: ")
        print(f"Type of material is {self.material}")
        print(f"No.of zip should be {self.zips}")
        print(f"No.of pocket should be {self.pockets}")

class Reebook(Mainfactory): #INHERITANCE
    def __init__(self, material, zips, pockets, colour):
        super().__init__("Reebook",material, zips, pockets)
        self.colour = colour

    def details(self):
        super().details()
        print(f"The colour of bag is {self.colour}")

class Nike(Mainfactory):
    def __init__(self, material, zips, pockets, colour, hidepocket):
        super().__init__("Nike",material, zips, pockets)
        self.colour = colour
        self.hidepocket = hidepocket
    
    def details(self):
        super().details()
        print(f"The colour of bag is {self.colour}")
        print(f"The No. of hidepocket is {self.hidepocket}")

reebook = Reebook("Leather", 3, 4, "Black")
reebook.details()

nike = Nike("polyster", 3,6,"Red",2)
nike.details()
