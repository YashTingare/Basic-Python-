class Person:
    name = "Yash Chintamani Tingare"
    occupation = "Data Science"
    age = 18
    skills = "Python, Numpy, Pandas, Jupyter Lab, Git, GitHub"
    def info(self):
        print(f"My name is {self.name}, I am {self.age} years old, and my occupation is {self.occupation}")


a = Person()
b = Person
a.info()
a.occupation = "Machine Learning"
print(a.occupation)

