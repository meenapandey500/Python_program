#List Comprehension
#to create a list which hold cube of number of list
'''A=[2,3,4,5,6,7,8]
new_list=[ ] #declare Empty list
for x in A:
    new_list.append(x**3)  # ** means find the power
print("List of Cube : ",new_list)  '''

#Use List Comprehension
A=[2,3,4,5,6,7,8]
new_list=[x**3 for x in A]
print(new_list)


