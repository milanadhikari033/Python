def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return a
    

a=24
b=43
c=25
print("The greatesr number is ",greatest(a,b,c))
    