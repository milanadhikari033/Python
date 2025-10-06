try:
    a=int(input("Enter the value of  a:"))
    b=int(input("Enter the value of  b:"))
    print(a/b)

except ZeroDivisionError as v:
    print("Infinite")
