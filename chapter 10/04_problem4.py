class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")
    def squareroot(self):
        print(f"The square root of {self.n} is {self.n**1/2}")
    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")
    @staticmethod
    def hello():
        print("Hello there")

a=Calculator(4)
a.hello()
a.square()
a.squareroot()
a.cube()