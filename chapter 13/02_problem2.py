name=input("Enter the name: ")
marks=input("Enter the marks: ")
phone=int(input("Enter the phone number: "))

# s=f"The name of the students is {name} , his marks are {marks} and his phone number is {phone}"
# print(s)

s="The name of the students is {} , his marks are {} and his phone number is {}".format(name, marks,phone)
print(s)