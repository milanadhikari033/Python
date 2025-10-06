class Complex:
    def __init__(self,r,i):
        self.i=i
        self.r=r

    def __add__(self,c2):
        return Complex(self.r+c2.r,self.i+c2.i)
    
    def __str__(self):
        return f"{self.r}+{self.i}i"
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)
    
c1=Complex(3,4)
c2=Complex(6,8)
print(c1+c2)
print(c1*c2)

