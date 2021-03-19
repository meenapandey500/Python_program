#filter function with lambda function
#suppose create list
X=[12,15,17,20,44,56,77,97]
#create a new list which hold odd no. from list x
result=list(filter(lambda a : a%2!=0 ,X))
print("list of odd nos. : ",result)
