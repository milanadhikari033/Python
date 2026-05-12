def main(): 
    try:
        n=int(input("Hey, Enter the number: "))
        print(n)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I am inside finally")

main()



"""Finally defines a block of code that always runs, no matter what happens —
even if an error occurs, or the program returns early."""