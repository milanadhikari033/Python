marks1=int(input("Ennter the marks of subject 1 : "))
marks2=int(input("Ennter the marks of subject 2 : "))
marks3=int(input("Ennter the marks of subject 3 : "))

total_percentage=(marks1+marks2+marks3)/3

if(total_percentage>44 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed by scoring  percentage:", total_percentage)

else:
    print("You are failed ! try next year!")