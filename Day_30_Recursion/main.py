def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(7))

# explane:
'''
first python will go to if condition and n is not equal to 0 or 1 
so 7 * 6
second python will go to if condition and n is not equal to 0 or 1 
so 7 * 6 * 5
Third python will go to if condition and n is not equal to 0 or 1 
so 7 * 6 * 5 * 4
fourth python will go to if condition and n is not equal to 0 or 1 
so 7 * 6 * 5 * 4 * 3
fifth python will go to if condition and n is not equal to 0 or 1 
so 7 * 6 * 5 * 4 * 3  * 2 
sixth python will go to if condition and n is not equal to 0 or 1 
so 7 * 6 * 5 * 4 * 3  * 2 * 1
SO ANSWER WILL
'''
