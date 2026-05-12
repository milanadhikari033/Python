try:
    n=int(input("Hey, Enter the number: "))
    print(n)

except Exception as e:
    print(e)

else:
    print("I am inside else")