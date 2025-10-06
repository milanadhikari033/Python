class Programmer:
    
    company="Microsoft"
    def __init__(self,name,salary,address):
        self.name=name
        self.salary=salary
        self.address=address

p=Programmer("Milan",9000000,"Ktm")
print(p.name,p.address,p.salary)