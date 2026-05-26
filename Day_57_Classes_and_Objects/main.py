class person:
    name = "Yash"
    age = 18
    occupation = "Data Science"
    networth = 20
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
# print(a.name, a.occupation)
a.info()
