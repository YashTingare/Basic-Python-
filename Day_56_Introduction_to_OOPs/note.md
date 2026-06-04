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
- It keeps data safe from being changed by mistake@
- It makes your code clean and easy to use@
- It gives control over what others can access or change.

