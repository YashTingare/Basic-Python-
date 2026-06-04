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

class Bag:
    def __init__(self, zips, material, pockets): # __init__ is constructor
        self.zips = zips
        self.material = material
        self.pockets = pockets

reebook = Bag(2, "Leather", 4)
print(f"I want {self.zips} zips ")

        

 