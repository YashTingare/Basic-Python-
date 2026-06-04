# f = open('Basic-Python-/Day_50_read()_readline()_and_other_methods/myfile.txt', 'r')

# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student {i} in Math is : {m1}")
#     print(f"Marks of student {i} in English is : {m2}")
#     print(f"Marks of student {i} in IT is : {m3}")
#     print(f"Percentage of student {i} is : {(m1+m2+m3)/300*100}")


# print(line)

#  ---------------------------------------------------------------------------------------

w = open("Basic-Python-/Day_50_read()_readline()_and_other_methods/myfile2.txt", "w")
lines = ["Hello I am Yash\n", "Starded Learning DS \n", "It is my promise that I will get intenship in my second year"]
w.writelines(lines)
w.close()
