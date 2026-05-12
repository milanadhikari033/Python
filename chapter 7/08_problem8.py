# '''
# *
# **
# ***
# ****
# '''

# n=int(input("Enter the numbers of terms:"))
# for i in range(1,n+1):
#     print("*"*(i),end="")
#     print("")

''' 
    *
   **
  ***
 ****
*****
'''
n=int(input("Enter the numbers of terms:"))
for i in range(1,n+1):
    print(" "*(n-i),end="") # if you donot give a space in the " " this will generate above program  output 
    print("*"*(i),end="")
    print("")