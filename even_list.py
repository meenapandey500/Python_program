#WAP to create the new_list which hold 1-20 even number
#Without using List Comprehension
'''even_list=[] #declare empty list
for i in range(1,21,1):
    if(i%2==0):
        even_list.append(i)
print("List of Even Number : ",even_list)'''

#WAP to create the new_list which hold 1-20 even number
#using List Comprehension
even_list=[i for i in range(1,21,1) if(i%2==0)]
print("List of Even Number : ",even_list)
