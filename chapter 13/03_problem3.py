n=int(input("Enter any number:"))
table=[str(n*i) for i in range (1 ,11)]

s="\n" .join(table)
print(s)