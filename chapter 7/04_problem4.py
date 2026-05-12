n=int(input("Enter any number: "))
for i in range(2,n):
    if(n%i==0):
        print("The given number is not a prime :",n)
        break
else:
    print("Number is prime:",n)