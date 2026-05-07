# def name(fname, Mname = "Chintamani", Lname = "Tingare"):
#     print("Hello",fname, Mname, Lname)

# name("Yash")


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i 
    print("Average is", sum/len(numbers))

average(2,2)