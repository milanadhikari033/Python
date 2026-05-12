# class Employee:
#     a=1
#     def show(cls):
#         print(f"The class attributes of a is {cls.a}")

# e=Employee()
# e.a=45
# e.show()

"""In the above code the value of a is 45 because instant attributes is executes first 
then the class  to print the class attributes with the presence of instant attributes 
we have use the class methods which is shown below : """


class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class attributes of a is {cls.a}")

e=Employee()
e.a=45
e.show()
