class Employee:
    def __init__(self):
        print("Constructor of Employee class")
    a=1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer class")
        b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__()      
        print("Constructor of Manager class")
    c=3

# o=Employee()
# print(o.a)

x=Manager()
print(x.c) 

# print(x.b)

# print(x.c)