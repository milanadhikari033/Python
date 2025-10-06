marks = { 
 "Harry":100,
 "Rohan":22,
 " Ramesh":44
}
# print(marks,type(marks))
# print(marks["Harry"])
# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"Harry":99,"Renuka":100})
print(marks)

print(marks.get("Harry2"))# this line checks there is presence or absence of Harry2
# and give none if absence and give the value if presence 

#print(marks["Harry2"])  This line gives the error if there is absence of a Harry2
