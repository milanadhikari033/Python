for i in range(10):
    if(i==5):
        break
    print(i)
# its output will be 0 to 4 because if (i==5) condtion is reached then break terminates 
# the program 

for i in range(10):
    if(i==5):
        continue
    print(i)

# when the above program is executed then  the compiler prints the 0 to 4 
# without any problem but when it reached i== 5 then it will continue from 
# the 6 to 9 in the above program.


# in simply means skip the iteration
