# def double(x):
#     return x*3

# line 1 and 2 is function and line number 6

# double = lambda x: x * 3
# print(double(20))

# add = lambda x, y: x + y
# print(add(2, 45))  

def fun(fx, value):
    return 6 * fx(value)

add = lambda x : x*x*x

print(fun(add, 2))