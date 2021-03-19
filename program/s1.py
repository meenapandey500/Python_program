import arithmetic
#write a program to find the sum of n nos.
n=int(input("How many nos . : "))

a=[] #declare empty list
for i in range(0,n,1):
    num=int(input("Enter number : "))
    a.append(num)
print(a)
ans=arithmetic.addition(a) #call function
print("sum of n nos. = ",ans)
