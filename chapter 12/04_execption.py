try:
    n=int(input("Hey, Enter the number: "))
    print(n)

except ValueError as v:
    print(v)

except Exception as e:
    print(e)

print("Thank you!")