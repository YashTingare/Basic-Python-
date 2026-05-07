Variable is like a container that holds data. 
Very similar to how our containers in kitchen holds sugar, salt etc 
Creating a variable is like creating a placeholder in memory and assigning it some value. 
In Python its as easy as writing:

## What is a Data Type?
Data type specifies the type of value a variable holds. 
This is required in programming to do various operations without causing an error.
In python, we can print the type of any operator using type function:

## These are four variables of different data types.
1. Boolean Data
2. Numeric Data
3. Complex
4. Text Data: String

```py
a = 1
b = None
c = "Yash"
d = True 
print("a is type of", type(a))
print("b is type of", type(b))
print("c is type of", type(c))
print("d is type of", type(d))
```

## Sequence Data: List
list: A list is an ordered collection of data with elements 
separated by a comma and enclosed within square brackets. 
Lists are mutable(we can change) and can be modified after creation.

```py
list1 = [8, 4.5, [-5, 9],["Yash", "naava"]]
print(list1)
```

## Sequenced data: Tuple
Tuple: A tuple is an ordered collection of data with elements 
separated by a comma and enclosed within parentheses. 
Tuples are immutable(we can not change) and can not be modified after creation.

```py
tuple = (("Yash", "Shreya"), ("lion", "Panda"))
print(tuple)   
```

## Mapped data: dict
dict: A dictionary is an unordered collection 
of data containing a key:value pair. 
The key:value pairs are enclosed within curly brackets YASH.

```py
dict1 = {"name":"nevr", "age":17, "canVote":False}
print(dict1)
dict2 = {"name":"Yash", "age":17, "canVote":False}
print(dict2)
```