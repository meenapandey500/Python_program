import sys 
#create dictionary for multiple students
students={'Name':['Anu','Seema','pankaj','rohan'],'Age':[32,43,21,56],'City':['Bhopal','Indore',
                                                            'Delhi','Mumbai']}
print(sys.getsizeof(students))
for x,y in students.items():                                                              
    print(x,":",y)
