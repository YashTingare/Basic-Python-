# Introduction to Loops
Sometimes a programmer wants to execute a group of statements a certain number of times.
This can be done using loops.
Based on this loops are further classified into following main types;
1. for loop
2. while loop

## The For Loop
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
```py
name  = "Yash"
for i in name:
     print(i)
```

## While Loop
We can even use the else statement with the while loop.
Essentially what the else statement does is that as soon
as the while loop condition becomes False, the interpreter
comes out of the while loop and the else statement is executed.
```py
count = 5
while (count > 0):
    print(count)
    count = count - 1
else:
    print("Babu")
```

## Range
What if we do not want to iterate over a sequence?
What if we want to use for loop for a specific number of times?

```py
for number in range(0, 13 , 6):
    print(number)

i = int(input("enter your valur :"))
while(i<=38):
    i = int(input("Enter your value : "))
    print(i)
print("Yash code done")
```