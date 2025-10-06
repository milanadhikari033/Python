def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)

n=int(input("ENter the number of terms:"))
print(f"The sum of {n} natural number is {sum(n)}")