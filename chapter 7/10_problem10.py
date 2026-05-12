n=int(input("Enter the number you want to generate multiplication table:"))
for i in range(1 ,11):
    print(f"{n}X{11-i}={n*(11-i)}")