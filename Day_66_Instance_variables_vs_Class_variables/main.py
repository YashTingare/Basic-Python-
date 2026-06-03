class Employee:
    companyname = "Apple" # This is class Variaable
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.21

    def showDetails(self):
        print(f"The name of employee in {self.companyname} is {self.name} and the raise amount is {self.raise_amount}")

emp1 = Employee("Yash")
# both are same
# emp1.showDetails()
#  OR 
Employee.showDetails(emp1)

emp2 = Employee("John")
emp2.raise_amount = 0.78 # This is Instance 
emp2.showDetails()