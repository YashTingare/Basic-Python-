class Employee:
    def __init__(self, name , ID):
        self.name = name
        self.ID = ID
    
    def showdetails(self):
        print(f"The name of employee is {self.name} and employee ID is {self.ID}")
    

class Programmer(Employee):
    def showlanguage(self):
        print("This is language use Python")

emp1 = Programmer("Yash", 11) 
emp1.showdetails()