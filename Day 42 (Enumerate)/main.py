marks = [23, 43, 2, 5, 8, 1, 21, 31, 43]

# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("Yash")
#     index +=1

#   👆 Both are same 👇

for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Yash")
   