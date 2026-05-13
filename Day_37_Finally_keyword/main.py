def func1():  
    try:
        l = [4, 6, 3, 8, 3, 98, 2,]
        i = int(input("Enter the value you want: "))
        print(l[i])
        return 1

    except:
        print("Neta thaka number")
        return 0

    finally:
        print("I am always executed")

x = func1()
print(x)