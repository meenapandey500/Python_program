#WAP to find the sum of elements present in the list using reduce function
from functools import reduce
def addition(a,b):
    return(a+b)

#main prgram
#Create List
X=[10,20,30,40,50]
result=reduce(addition,X)
print("Sum of elements of list X : ",result)
