marks=int(input("Enter the marks of student: "))
if(marks<=100 and marks>=90):
    print("Your grade isEx")
elif(marks<90 and marks>=80):
    print("Your grade isA")
elif(marks<80 and marks>=70):
    print("Your grade isB")
elif(marks<70 and marks>=60):
    print("Your grade isC")
elif(marks<60 and marks>=50):
    print("Your grade isD")
elif(marks<50):
    print("Your grade is Fail")


    ''' also you can change the above code by not printing in the condition just by making 
   ( grade = Ex) like this and finally prints  the grade after checking all conditions of the 
   above situation which reduces the efforts of the code 
    '''
