'''
    *
   ***
  *****
 *******

'''
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):                # Outer loop → rows
    for j in range(1, n + i):            # Inner loop → spaces + stars combined
        if j <= n - i:
            print(" ", end="")           # Print spaces first
        else:
            print("*", end="")           # Then print stars
    print()                               # Move to next row

# Alternative way:

n=int(input("Enter the numbers of terms:"))
for i in range(1,n+1):
    print(" "*(n-i),end='')
    print("*"*(2*i-1),end="")
    print("")

 
'''
* 
* * 
* * * 
* * * *
'''
n=int(input("Enter the numbers of terms :"))
for i in range ( 1 ,n):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

'''* * * *
   * * * *
   * * * *
   * * * *'''

n=int(input("Enter the numbers of terms :"))
for i in range ( 1 ,n):
    for j in range(1,n):
        print("*",end=" ")
    print()


'''* * * *
   * * * 
   * * 
   *'''


n=int(input("Enter the numbers of terms :"))
for i in range ( n,0 ,-1):
    for j in range(i):         # we can alternately write for j in range(0,i)
        print("*",end=" ")
    print()

