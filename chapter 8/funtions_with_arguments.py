'''# funtions with arguments
def function(name, ending):
    print("Good morning , "+ name)
    print(ending)

function("Harry", "Thank you!")
function("Rohan","Thank you!")
function("Rahul","Thanks") '''



def function(name, ending):
    print("Good morning , "+ name)
    print(ending)
    return 'ok'
 # if does not return it will printt none but in our case
 # we have return ok so there will be print ok 

a=function("Harry", "Thank you!")
print(a)

