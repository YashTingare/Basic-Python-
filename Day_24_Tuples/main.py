tup = (1, 5, 6, "Yash", 3.0, True)
print(type(tup))
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[4])

if "Yash" in tup:
    print("He is smart boy....")
else:
    print("There no smart boy in Tup")

tup2 = tup[1:4]
print(tup2)