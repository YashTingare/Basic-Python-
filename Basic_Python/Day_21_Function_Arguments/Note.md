# FUNCTION ARGUMENTS AND RETURN STATEMENT

# There are four types of arguments that we can provide in a function:
   1. Default Arguments
   2. Keyword Arguments
   3. Variable length Arguments
   4. Required Arguments

# DEFAULT ARQUMENTS
  We can provide a default value while creating a funtion. This way the function assumes a default value if a value is not provided in the function call for that argument.

Example:
```py
def name(fname, Mname = "Chintamani", Lname = "Tingare"):
    print("Hello",fname, Mname, Lname)

name("Yash")
```
# KEYWORD ARDUMENTS:
We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

Example:

```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
```
Output:
```
Hello, Jade Peter Wesker
 ```

# REQUIRED ARGUMENTS:
In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

Example 1:  
when number of arguments passed does not match to the actual function definition.

```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill")
```
Output:
```
name("Peter", "Quill")\
TypeError: name() missing 1 required positional argument: 'lname'
 ```

Example 2: 
when number of arguments passed matches to the actual function definition.

```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")
```
Output:
```
Hello, Peter Ego Quill
 ```

# VERIABLE-LENGTH ARGUMENTS:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:

# ARBITRARY ARGUMENTS:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

Example:
```python
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")
```
Output:
```
Hello, James Buchanan Barnes
 ```

# KEYWORD ARBITRARY ARGUMENTS:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

Example:
```python
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")
```
Output:
```
Hello, James Buchanan Barnes
```

## return Statement
The return statement is used to return the value of the expression back to the calling function.

Example:
```python
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))
 ```

Output:
```
Hello, James Buchanan Barnes
```