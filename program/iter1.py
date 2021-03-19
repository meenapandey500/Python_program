str="Meena Pandey" #string work as list 0- M 1-e 2-e
#if large amt of string value then use iterable : iter( ) inbuilt function
for c in str:
    print(c)
#if large amt of string value then use iter( )
x=iter(str)
print(x)
print(x.__next__()) #use iterator method __next__() 
print(x.__next__())
for i in x:
    print(i)
