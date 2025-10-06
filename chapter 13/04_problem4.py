def divisible5(n):
    if(n%5==0):
        return True
    return False

a= [22,255,10,55,95,65,100,20]
f=list(filter(divisible5,a))
print(f) 