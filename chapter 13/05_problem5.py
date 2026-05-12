from functools import reduce
l= [22,55,10,55,75,65,10,20]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))

