# MAP

# def cube(x):
#     return x*x*x

# print(cube(2))

#      OR 

# def cube(x):
#     return x*x*x

# l = [2,98,3,6,4]

# newl = list(map(cube, l))
# print(newl)

# ------------------------------------------

# FILTER

# l = [2,98,3,6,4]

# def filter_function(a):
#     return a>3

# newnewl = list(filter(filter_function, l))
# print(newnewl)

# ------------------------------------------

#  REDUCE

# from functools import reduce

# l = [2,1,2,3]

# def mycube(x, y):
#     return x + y

# cube = reduce(mycube, l)

# print(cube)