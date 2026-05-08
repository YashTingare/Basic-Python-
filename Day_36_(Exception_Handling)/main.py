a = input("Enter your number:")
print(f"Multipication table of {a} is :")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {int(i)} = {int(a)*i}")
except:
    print("Invalid Input")

print("End th program")