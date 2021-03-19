#create tuple
A=(12,45,67,89,90) #only max() and min() apply in tuple
print(A)
#find the sum of element
#first convert tuple to list and then sum
s=sum(list(A)) #list(A) change tuple in list
print("Sum : ",s)
#sorting means to arrange elements in ascending order
#first convert tuple into list
L=list(A)
L.sort() #ascending order
print(L)
L.reverse()
print(L)

#to convert tuple type data to list type then use list(tuplename)
B=list(A)
print(B)
B.append(29)
print(B)
#convert B list to tuple
T=tuple(B)
print("tuple : ",T)
