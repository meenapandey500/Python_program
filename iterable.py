#Iterable(__iter__()/__getitem__() :  use for string variable : work as List variable
#for eg.
'''name="Meena"
for i in name:
    print(i)'''

#use __iter__() method (If large amt of string value 
name="Meena"
x=iter(name) #we traverse means retrieve string iterator
#here x is string iterator object at memory location
print(x)
print(x.__next__())
print(x.__next__())

for i in x:
    print(i)
