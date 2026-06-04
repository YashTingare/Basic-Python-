# Length of a String:
"""We can find the length of a string using len() function."""
# Ex
Book = "Starwar"
len1 = len(Book)
print("Starwar ia a", len1, "letter word")

# String as an array:
"""A string is essentially a sequence of characters also called an array.
Thus we can access the elements of this array."""
# Ex
word = "Psychology"
print(word[3:5])    #Including 3 but not 5    (Slicing in between)
print(word[-4:-2])  #Including -4 but not -2  (Slicing using negative index)
print(word[:6])     #Including 0 but not 6    (Slicing from start)
print(word[9:])     #Including 9 but not 0    (Slicing till end)
print(len(word))

# Note: This method of specifying the start and end index to specify a part of a string is called slicing.
print("i love you babu")