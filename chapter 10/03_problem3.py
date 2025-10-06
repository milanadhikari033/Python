class Demo:
    a=4

o=Demo()
print(o.a) #prints the class attributes because absence of instant attributes
o.a=0 # sets the instant attributes 
print(o.a) # prints the instant attributes 
print(Demo.a) # prints the class attributes 
