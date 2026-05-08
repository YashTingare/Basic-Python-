## TYPECASTING IN PYTHON
The conversion of one data type into the
other data type is known as type casting
in python or type conversion in python.

Python supports a wide variety of functions
or methods like: 
1. int()
2. float()
3. str()
4. ord(),
5. hex()
6. oct()
7. tuple()
8. set()
9. list()
10. dict()

For the type casting in python.

## Two Types of Typecasting:
1. Explicit Typecasting
2. Implicit Typecasting

## Explicit Typecasting:
The conversion of one data type into another data type,
done via developer or programmer's intervention or manually as per the requirement,
is known as explicit type conversion.

It can be achieved with the help of Python’s built-in type
conversion functions such as int(), float(), hex(), oct(), str(), etc.

```py
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)
```

## Implicit type casting:
Data types in Python do not have the same level i.e.
ordering of data types is not the same in Python.
Some of the data types have higher-order, and some have lower order.
While performing any operations on variables with different data types in Python,
one of the variable's data types will be changed to the higher data type.
According to the level, one data type is converted into other by the Python interpreter itself (automatically).
This is called, implicit typecasting in python.

Python converts a smaller data type to a higher data type to prevent data loss.
```py
c = 2.9
d = 3 #Implicit convert "d" into float because "c" is add in "d" and c is float.
g = c + d
print(type(g))
```