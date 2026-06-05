# Object-Oriented Programming (OOP) 

- Make your code more reusable
- Easier to work with large program
- OOP program prevent you from repeating code
- OOP provide you security.

## What are Classes? 
A class is a blueprint for creating object. There are 2 types of thing inside class Attributes and Methodes.

- Attributes - Variables defined inside the class are Attributes.
- Methods - Function defined inside the class are Methods

## What is Encapsulation?
In programming, Encapsulation is about keeping some information (Data) safe and only letting it be change or looked at in specific ways.

## What is Ploymorphism?
Ploymorphism means having many forms.

## What is Inheritance?
When one class inherits(receives) some feature from another class this phenomena is know as inheritance.

## What is Abstraction?

When we only see the essential part of our code and hides the rest is the process of Abstraction.

## What is Constructor?
A constructor is a method that runs automatically when we call a class and this constructor function will target the objects location.
> **Note:**
>>**To target the objects loctaions we use self keywords**

```py
class Bag:
    def __init__(self, zips, material, pockets): # __init__ is constructor
        self.zips = zips
        self.material = material
        self.pockets = pockets

reebook = Bag(2, "Leather", 4)
print(reebook.zips)
print(reebook.material)
print(reebook.pockets)
```

## Type of Attributes & Methods

### Attributes
- Class attribute: A normal variable created inside a class is attribute and thats it.

- Instance attribute:  A attribute created using an instance like self.name, self.age etc. It is known as instance attributes


### Methods

-  Instance Method:  An instance method Works with instance (object) of the class. This method can access and modify instance attributes.

- Class Method: This method works with the class itself it will not target the instance (object). we have to use @classmethod decorator for creating the class method and it takes cls as their first parameter.

- Static Method: This method doesn’t access class or instance directly it also uses a decorator @staticmethod it just acts like a regular function placed inside a class.

```py
class Aminal:
    king = "lion" # Class Attributes

    def __init__(self, name):
        self.name = name # Instance/object Attributes

    def hello(self): # Instance/object Method (Captures the location of object)
        print(f"I will capture the loctaion of objects {self.name}")

    @classmethod
    def details(cls): # Class Methods captures the location of class
        print(f"I will capture the location of classes {cls.king}")

    @staticmethod
    def greeting(): # this is static method it will not capture the location of class and object
        print("Good morning")
```

## Inheritance

Inheritance allows a class (child class) to inherit properties and behaviors (attributes and methods) from another class (parent class)1

### Constructor in Inheritance 

Lets say you have created a parent class with a constructor function inside it and then this class is inherited by another class then the constructor function of parent class will work for the child class as well. 

### Types of Inheritance
- Single Inheritance: All the inheritance we saw above was single level.
- Multiple Inheritance: Multiple Inheritance means there will be 2 parent classes and only 1 child class and the child class will inherit all the attributes and methods of both parents.
- Multilevel Inheritance: This is a basic case where we will have
* grandparent class → parent class → child class
* The attributes and methods are passed on through all the
classes.

> **Note:**
>> **The constructor function will be inherited of the first class that has been Inherited. This is MRO(Method Resolution Order) followed by python.**

```py
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

## Multi level Inheritance
class Nike(Mainfactory):
    def __init__(self, material, zips, pockets, colour, hidepocket):
        super().__init__("Nike",material, zips, pockets)
        self.colour = colour
        self.hidepocket = hidepocket
    
    def details(self):
        super().details()
        print(f"The colour of bag is {self.colour}")
        print(f"The No. of hidepocket is {self.hidepocket}")

class Campus(Reebook):
    def __init__(self, material, zips, pockets, colour, size):
        super().__init__(material, zips, pockets, colour)
        self.size = size
    
    def details(self):
        super().details()
        print(f"The bag size should be {self.size}")

reebook = Reebook("Leather", 3, 4, "Black")
reebook.details()

nike = Nike("polyster", 3,6,"Red",2)
nike.details()

campus = Campus("Plastic", 4, 6, "Gold", "60 liters")
campus.details()
```

```py
# Multiple Inheritance
class Animals:
    def __init__(self, name):
        self.name = name

class Human:
    def __init__(self, ID):
        self.ID = ID

class Robots(Animals, Human):
    def __init__(self, name, ID):
        Animals.__init__(self, name)
        Human.__init__(self, ID)

robo = Robots("Yash", 11)
print(robo.name)
print(robo.ID)
```

## Polymorphism 

Polymorphism is a core concept in Object-Oriented Programming (OOP). The word means "manyforms" — and in programming, it allows the same interface or method name to behave differently depending on the object or context.

### Types of Polymorphism

- Method Overridingo: This is where a child class overrides a method of the parent class, and Python decides at runtime which method to call, based on the object type.

```py
class Human:
    def speak(self):
        print("I am yash and i can speak")

class Animals:
    def speak(self):
        print("I cant speak")


obj1 = Human()
obj1.speak()
obj2 = Animals()
obj2.speak()


Method Overriding (we need Inheritance)

class Animals:
    a = 12
    def __init__(self, name):
        self.name = name

    def details(self):
        print(f"Your name is {self.name}")

class Humans(Animals):
    b = 13
    def details(self):
        print(f"Your info is {self.name}")

obj = Humans("Yash")
obj.details()
```

## Encapsulation
1.  Encapsulation means putting data (variables) and code (functions) together in one place — inside a class
2.  It also means hiding the internal details of how things work, and only showing what is needed@
- It keeps data safe from being changed by mistake
- It makes your code clean and easy to use@
- It gives control over what others can access or change.


### Access modifiers in python

Access modifiers means how we give access of our attributes
and methods to the object or inherited classes. There are 3 types
lets see them one by one.

1. **Public Attributes and Methods:** Till now every attribute and methods we have created are public means the inherited classes and objects can access them no matter what
2.  **Protected Attributes and Methods:** 
- python protected members are created using a single underscore but it still can be accessed from outside the class so you might wonder whats the point of using them
- Python doesn’t enforce protected access like other languages (e.g., Java or C++). But it uses a naming convention to tell developers.
3. **Private Attributes and Method:**
- It cannot be accessed from outside the class — only from
inside the class where it is defined
- In Python, we use two underscores (__) before the name to
make it private.

```py
class Demo:
    __company = "BMW"       # Private Class Attributes
    ID = 11                 # Public Class Attributes
    def __init__(self):
        self.name = "Yash"          # Public Object Attributes
        self._age = 19              # Protected Object Attributes
        self.__salary = "$275000"   # Private Object Attributes

    def show(self):                         # Public Method
        print("Inside the class: ")
        print("Public", self.name)          
        print("Protected", self.age)        
        print("Private", self.__salary)      


obj = Demo()
print(obj.name)
print(obj._age)
print(obj.__salary) # It will through the error becuase it is private attributes
```

## Abstraction 

- Abstraction does not exist in python but we can achieve it using a library we will see what is a library later.
- Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details.
- It is used to define a common interface for different subclasses 

### Abstract classes and methods 

- Abstract classes are classes that contains one or more abstract methods.
- A method that is defined but not implemented in the abstract class. subclasses must provide the implementation.

```py
from abc import ABC, abstractmethod

class enforce(ABC):
    @abstractmethod
    def enginestart():
        print("Start the engine with biomatrics")

class Bike(enforce):
    def enginestart(self):
        print("Bike is Started")

class Car(enforce):
    def enginestart(self):
        print("Car is started")

class Truck(enforce):
    pass

obj1 = Bike()
obj1.enginestart()
obj2 = Car()
obj2.enginestart()
obj3 = Truck()      # It will give error because we didnt use enginestart()
obj3.enginestart()
```

## Dunder methods

- Dunder methods are special methods in Python that start and end with double underscores, like __init__, __str__, __add__, etc.
- They automatically get called when you perform certain actions on an object.
- They help you
    - Customize behavior of your clasT
    - Make your class objects behave like built-in data types (like strings, lists, etc.)

```py
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello my name is {self.name}"
    
obj = Animal("Lion")
print(obj)
```


## Decorator

- A decorator is just a function that modifies another function without changing its actual code.
- Imagine you have a cake (your function). A decorator is like putting icing on the cake. It doesn’t change the cake itself, but makes it better, prettier, or adds some new flavor!
- For creating a decorator you first have to create a decorator functions and then inside that we will create a wrapper.
- Its tough to understand with text see the video

```py
def extragreeting(func):
    def wrapper():
        print("Hello I am Yash Tingare")
        func()
        print("Thank You for everything")
    return wrapper

@extragreeting
def greetings():
    print("Good Morning")

greetings() 
```

## Args and Kwargs 

They’re special keywords in Python used in function definitions to accept a flexible number of arguments.
* Now you always don’t have to use Args and Kwargs the main thing is * , ** you can use any names in front of them.
* so *args are used for multiple positional arguments, and **kwargs are used for multiple key word arguments.
* And the *args becomes a tuple and **kwargs becomes a dictionary
* The use case is great
    * You don’t need to know how many inputs you'll get%
    * Helps in building flexible functions, decorators, APIs, and more.

```py
## *args
def extragreeting(func):
    def wrapper(*args, **kargs):
        print("Hello I am Yash Tingare")
        func(*args, **kargs)
        print("Thank You for everything")
    return wrapper

@extragreeting
def addition(a,b,c):
    print(a+b+c)

addition(20,56,42) 

# **kargs
def info(**kargs):
    pass
info(name = "Yash", age = 24, hight = "5'11")
```