#write a program to create a mini calculator
a=float(input("Enter First Number : "))
b=float(input("Enter Second Number : "))
print("press 1 for sum")
print("press 2 for subtract")
print("press 3 for multiply")
print("press 4 for divide")

choice=int(input("Enter your choice : "))
if(choice==1):
    c=a+b
    print("Sum : ",a,"+",b,"=",c)

elif(choice==2):
    c=a-b
    print("subtract : ",a,"-",b,"=",c)
elif(choice==3):
    c=a*b
    print("multiply : ",c)
elif(choice==4):
    c=a/b
    print("divide : ",c)
else:
    print("invalid choice")
