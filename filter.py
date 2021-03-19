#Use of filter( ) with lambda
#WAP A list contains both even and odd numbers
#create a List
N=[12,34,56,23,15,18,19,20] #input list
print("Input List : ",N)
even_list=list(filter(lambda x : x%2==0,N))
print("List of Even Nos. : ",even_list)
odd_list=list(filter(lambda x : x%2!=0,N))
print("List of odd Nos. : ",odd_list)
