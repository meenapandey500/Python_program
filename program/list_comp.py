#Generator
#for example :
'''a=[i for i in range(0,999999999)] #here create a list a which hold no. 0 to 8
print(a)'''
#syntax of list comprehension
# [expression  for var in range()]
#we have large amt of data hold in list then program crash after run means given memory error
#so solve this problem we use generator , we not create list
#create a generator ,replace square bracket[ ] with parenthesis ( )
a=(i for i in range(0,99999999999)) #here a generator object
print(a)
print(a.__next__())
print(a.__next__())
#use __next__( ) : inbuilt method of iterator ,
#its retrieve,traverse value from one by one from generator

#show value from generator then use iterator
'''for item in a:
    print(item)'''
