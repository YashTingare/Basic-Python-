x = 4
print(x)

def hello():
    global x
    x = 6
    print("Hello Yash")
    print(x)
    
hello()