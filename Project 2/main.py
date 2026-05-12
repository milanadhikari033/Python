import random
n=random.randint(1,100)
a=-1
gusses=1
while(a!=n):
    a=int(input("Guess the number:"))
    if(a>n):
        print("Lower number please!")
        gusses+=1
    elif(a<n):
        print("Higher number please!")
        gusses+=1
print(f"You have gusses the {n} number correctly {gusses} attempt")
