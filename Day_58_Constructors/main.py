class Person:
    # __init__ it is a Constructors it will always run when you run Person class
    def __init__(self, n, o):
        self.name = n
        self.occ = o
    def info(self):
        print(f"Hello I am {self.name} and my occupation is {self.occ}")

a = Person("Yash Chintamani Tingare", "Data Science") # these are 2 arguments in from of n and o in constructor
a.info()