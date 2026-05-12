class Number:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
        return self.n+num.n

n=Number(3)
m=Number(4)
print(m+n)


"""IN the above code   { def __add__(self,num):}  this function is used as operator 
overloading concept in the python programming """
