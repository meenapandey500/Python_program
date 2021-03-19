#List Comprehension  : -

#a=[x for x in range(0,99999099999999)]    #here a is a list object stop=99998
#print(a)
#use Generator
a=(x for x in range(0,99999099999999)) # here a is a generator object
print(a)
#to iterate the number from genrator object if you need
for item in a:
    print(item)
