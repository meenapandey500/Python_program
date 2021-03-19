#6. Identity operator
#There are 2 types of Identity operator
# 1. is  2. is not
#for eg.
#we create the list X and Y
X=["apple","banana"]
Y=["apple","banana"]

Z=X
print(X is not Z) #return False because Z is the same object as X

print(X is not Y) #return true because X is not the same object as Y ,
#even if they have the same content

print(X==Y) #return True because == check the content of X and Y 
