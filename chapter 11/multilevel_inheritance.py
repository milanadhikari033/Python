class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=3

o=Employee()
print(o.a)
# print(o.b) cannot be execute because absence of b in Employee class 

x=Manager()
print(x.a) # it prints because manager class can access the Programmer and Programmer 
#class can access the Employee class and finally manager class can access on employee

print(x.b)

print(x.c)