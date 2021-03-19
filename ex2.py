#Exception handling : to handle run time error

a=int(input("Enter number a : ")) #20     but a=20
b=int(input("Enter number b : ")) #10     but b=10
c=int(input("Enter number c : "))#5        but c=10
try:
    d=a/(b-c)  #d=20/(10-5) means d=20/5 means d=4   d=20/(10-10) means d=20/0 means
except ZeroDivisionError:   #ZeroDivisionError inbuilt class for divide by zero error
    print("Divide by zero error ")
else:
    print("result=",d) 

print("Bye-Bye")
