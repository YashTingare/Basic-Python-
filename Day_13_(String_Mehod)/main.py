a = "!!!!!!!!!Yas h!!!!!!!!!!!!"

print(len(a))

print(a.upper())                  #upper(): The upper() method converts a string to upper case.

print(a.lower())                  #lower(): The lower() method converts a string to lower case.

print(a.rstrip("!"))              #rstrip(): the rstrip() removes any trailing characters.

print(a.replace("Yash", "Smart")) #replace(): The replace() method replaces all occurences of a string with another string.

print(a.split(" "))               #split(): The split() method splits the given string at the specified instance and returns the separated strings as list items.

heading = "my name is yAsh"
print(heading.capitalize())       #Capitalize(): The capitalize() method turns only the first character of the string to uppercase and the rest other characters of string are turned to lowercase. The string has no effect if the first character is already uppercase.

yash = "Lets go to home"

print((yash.center(80)))         #Center(): The center() method aligns the string to the center as per the parameters given by the user.

print(yash.count("e"))           #Count(): The count() method returns the number of times the given value has occurred within the given string.

print(yash.endswith("o"))        #endswith(): The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

print(yash.endswith("g", 1, 7)) #find(): The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

print(yash.find("go"))          #find(): The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

print(yash.index("t"))          #index(): The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

str1 = "WelcomeToTheConsole"
print(str1.isalnum())           #isalnum(): The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

isalpha = "WelcomePagal"
print(isalpha.isalpha())        #isalpha(): The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

islower1 = "Yash IS a sMart boY"
print(islower1.islower())       #islower(): The islower() method returns False if the characters in the string are upper case

islower2 = "yash is a smart boy"
print(islower2.islower())       #islower(): The islower() method returns True if the characters in the string are lower case,

isupper = "YASH"
print(isupper.isupper())        #isupper(): The isupper() method returns True if all the characters in the string are upper case, else it returns False.

startwith = "Yash is smart boy"
print(startwith.startswith("Yash"))  #startswith(): The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

swapcase = "Python is a Good "
print(swapcase.swapcase())          #swapcase(): The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

title = "let's play the game"
print(title.title())                #title(): The title() method capitalizes each letter of the word within the string.