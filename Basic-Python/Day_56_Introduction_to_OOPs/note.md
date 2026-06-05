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

## Type of Attributes & Methods

### Attributes
- Class attribute: A normal variable created inside a class is attribute and thats it.

- Instance attribute:  A attribute created using an instance like self.name, self.age etc. It is known as instance attributes


### Methods

-  Instance Method:  An instance method Works with instance (object) of the class. This method can access and modify instance attributes.

- Class Method: This method works with the class itself it will not target the instance (object). we have to use @classmethod decorator for creating the class method and it takes cls as their first parameter.

- Static Method: This method doesn’t access class or instance directly it also uses a decorator @staticmethod it just acts like a regular function placed inside a class.

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

## Polymorphism 

Polymorphism is a core concept in Object-Oriented Programming (OOP). The word means "manyforms" — and in programming, it allows the same interface or method name to behave differently depending on the object or context.

### Types of Polymorphism

- Method Overridingo: This is where a child class overrides a method of the parent class, and Python decides at runtime which method to call, based on the object type.

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

## Abstraction 

- Abstraction does not exist in python but we can achieve it using a library we will see what is a library later.
- Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details.
- It is used to define a common interface for different subclasses 

### Abstract classes and methods 

- Abstract classes are classes that contains one or more abstract methods.
- A method that is defined but not implemented in the abstract class. subclasses must provide the implementation.

## Dunder methods

- Dunder methods are special methods in Python that start and end with double underscores, like __init__, __str__, __add__, etc.
- They automatically get called when you perform certain actions on an object.
- They help you
    - Customize behavior of your clasT
    - Make your class objects behave like built-in data types (like strings, lists, etc.)
