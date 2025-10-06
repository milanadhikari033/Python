class Employee:
    salary=1600000  
    address="ktm"
    def __init__(self,name,address,salary):#Dunder method which is automatically called  
        self.name=name
        self.address=address
        self.salary=salary
        print("I am creating a object")
    def getinfo(self):
        print(f"The salary is {self.salary}\nThe address is {self.address}")

    @staticmethod
    def greet():
        print("Good Morning")

e=Employee("Milan","Pokhara",150000)
print(e.name ,e.salary,e.address)

# f=Employee()
