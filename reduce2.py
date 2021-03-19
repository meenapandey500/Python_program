#WAP to find the sum of elements present in the list using reduce function with lambda
from functools import reduce


#main prgram
#Create List
X=[10,20,30,40,50]
result=reduce(lambda a,b : a+b,X)
print("Sum of elements of list X : ",result)
