# FUNCTION ARGUMENTS AND RETURN SATEMENT

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

