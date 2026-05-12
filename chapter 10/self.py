class Employee:
    salary=1600000  
    address="ktm"
    def getinfo(self):
        print(f"The salary is {self.salary}\nThe address is {self.address}")

    @staticmethod
    def greet():
        print("Good Morning")

e=Employee()
# e.getinfo()
Employee.getinfo(e)
e.greet()
# just  above two line works same 