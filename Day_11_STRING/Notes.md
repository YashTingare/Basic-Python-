## What are strings?
In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.
```py
yash = 'yash'
print("hii " + yash)
```

## NOTE
It does not matter whether you enclose your strings in single or double quotes,
the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings.
Example, consider the sentence: He said, “I want to eat an apple”.
```py
yash = 'yash'
print(yash + ' said "you the best code"')
```
## Multiline Strings:
If our string has multiple lines, we can create them like this:
```py
a = """ 
Yash
Kritika
Shreya
Ganesh
Sytham
Vedika
Mudukli
"""
print(a)
```

## Accessing Characters of a String:
In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string
```py
b = "Shreya is a pagal girl"
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[5])
```
## Looping through the string:
```py
for character in b:
    print(character)
```