'''
f=open("morefile.txt")
print(f.read())
f.close()
'''
# The same code is written through the below code
with open("morefile.txt")  as f:
    print(f.read())
#Here is no need of the file cose with the withopen(statement())
