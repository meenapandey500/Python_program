#Write a program to create a list which hold those no. which is divisible by 2 and 5 of number 1-101

#  10  20  30 40 50 60 70 80 90 100
#without using listcomprehension
A=[]
for x in range(1,101):
    if(x%2==0):  #outer if
        if(x%5==0):  #inner if
            A.append(x)
print(A)


#Using list comprehension  with nested if
A=[x for x in range(1,101) if(x%2==0) if(x%5==0)]
print(A)
