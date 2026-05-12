class Employee:
    company="Apple"
    def show(self):
        print(f"The name  is {self.name}\nThe salary  is{self.salary}")
# class programmer:
#     def show(self):
#         print(f"The name  is {self.name}\nThe salary  is{self.salary}")
#     def showlanguage(self):
#         print(f"The name is {self.name} and he is good at {self.language}")

class Programmer(Employee):
    company="Microsoft"
    def showlanguage(self):
         print(f"The name is {self.company} and he is good at {self.language}")

a=Employee
b=Programmer
print(a.company, b.company)



