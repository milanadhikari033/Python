class Employee:
    company="Apple"
    name="Rajesh"
    def show(self):
        print(f"The name  is {self.name}\nThe company  is {self.company}")

class Coder:
    language="Python"
    def printLanguage(self):
        print(f"Out of all languages here is  your language: {self.language}")
    

class Programmer(Employee, Coder):
    company="Microsoft"
    def showlanguage(self):
         print(f"The name is {self.company} and he is good at {self.language}")

a=Employee()
b=Programmer()

b.show()
b.printLanguage()
b.showlanguage()


