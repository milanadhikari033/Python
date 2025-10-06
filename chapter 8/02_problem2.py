def f_to_c():
    return 5*(f-32)/9
f=int(int(input("ENter the number in the F: ")))
c = f_to_c()
print(f"{round(c,2)}°C")
# here is round function is used to many number after decimals in input to make only 2