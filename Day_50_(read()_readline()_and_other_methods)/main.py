# f = open('Day 50 (read() readline() and other methods)\myfile.txt', 'r')
# i = 0

# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student {i} in Math is: {m1*100/100}")
#     print(f"Marks of student {i} in Science is: {m2*100/100}")
#     print(f"Marks of student {i} in IT is: {m3*100/100}")
#     print(line)

f = open('Day 50 (read() readline() and other methods)\myfile2.txt', 'w')
lines = ["line 1", "line 2"]
for line in lines:
    f.write(line + "\n")
f.close()