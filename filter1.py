#Use of filter( ) with normal function
#syntax of filter()
#filter(userdefinedfunction,input list)
#WAP A list contains both even and odd numbers
def even(x):
    if(x%2==0):
        return x
def odd(x):
    if(x%2!=0):
        return x
#main program
#create a List
N=[12,34,56,23,15,18,19,20] #input list
print("Input List : ",N)
even_list=list(filter(even,N))
print("List of Even Nos. : ",even_list)
odd_list=list(filter(odd,N))
print("List of odd Nos. : ",odd_list)
