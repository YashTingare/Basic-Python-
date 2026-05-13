# Finally Clause

The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

### Syntax:

```py
try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation
```

The finally block is executed irrespective of the outcome of try……except…..else blocks
One of the important use cases of finally block is in a function which returns a value.

### Example:

```py
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")
```

# IT WILL ASK IN INTERVIEW
## WHY FINALLY USE?
### ANSWER: To define a section of code that must execute regardless of whether an exception occurs or not
 1. Resource Management: Ensuring that external resources are properly released, such as closing files, shutting down database connections, or releasing network sockets.
 2. Guaranteed Execution: Unlike code placed after a try-except block, the finally block runs even if an exception is unhandled (re-raised) or if the program exits the block via a return, break, or continue statement.