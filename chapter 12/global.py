a=89
 
def fun():
    global a
    a=3
    print(a)

fun()
print(a)

"""In the above code global is used to make the variable a as a global after making the 
it prints a as 3 """