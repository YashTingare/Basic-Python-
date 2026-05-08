# NOTES

## Break
The break statement enables a program to skip over a part of the code.
A break statement terminates the very loop it lies within.

``` py
for i in range(12):
    print("5 X", i+1, "=", 5*(i+1))
    if (i==9):
        break

print("Yes")
```

## Continue Statemant
The continue statement skips the rest of the loop statements and causes the next iteration to occur.

``` py
for i in range(18):
    if(i==9):
        print("Skip the Iteration")
        continue
    print("2 X", i, "=", 2*i)
```

## Do While Loop
```py
i = 0
while True:  # while ture means infinite loop
    print(i)
    i = i+1
    if(i%100==0):
        break`
```