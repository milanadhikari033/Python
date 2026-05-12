a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

if(b==0):
    raise ZeroDivisionError("Hey! Our program is not meant by division by zero")
else:
    print(f"The divsion is {a/b}")