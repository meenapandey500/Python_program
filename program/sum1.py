#import library1 as lib  #call library file
from library1 import *  # * means all function actibe
while(True):
    menu()
    ch=int(input("Enter your choice"))
    if(ch==5):
        break #exit from loop
    else:
        a=int(input("Enter number a : "))
        b=int(input("Enter number b : "))
        if(ch==1):
            z=addition(a,b) #call function  , here a and b are actual parameters /arguments
            print("sum=",z)
        elif(ch==2):
            z=subtraction(a,b)
            print("subtraction=",z)
        elif(ch==3):
            print("multiply=",multiply(a,b))
        elif(ch==4):
            z=divide(a,b)
            print("divide = ",z)
        else:
            print("Invalid choice " )
