#use list comprehension 
#a=[x  for x in range(0,99999999999)]  #here a is list object
#print(a)  

#we use generator means we replace [ ] with ( )
a=(x  for x in range(0,99999999999)) #here a is generator object
print(a)
#if you want to print nos. then  can be do iterate
#iterate 
for item in a: 
    print(item)

#generator is used to process large amount of data 

