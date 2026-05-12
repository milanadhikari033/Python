from functools import reduce

# Map Exmaples
l=[1,3,4,5,7,8,45,3]

square= lambda x:x*x

sqList= map(square,l)
print(list(sqList))


#Filter example
 
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven=filter(even,l)
print(list(onlyEven))


# Reduce example 
def sum(a,b):
    return a+b

mul=lambda x,y:x*y
print(reduce(sum ,l))
print(reduce(mul ,l))