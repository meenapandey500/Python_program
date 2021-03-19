#Example of method overloading
import math
class shape:
    def area(self,a=None,b=None,c=None):
        if(a!=None and b==None and c==None): #area of circle means send radius =a
            print("Area of circle : ",3.14*a*a)
        elif(a!=None and b!=None and c==None): #area of rectangle means length=a , breadth=b
            print("Area of rectangle : ",a*b)
        elif(a!=None and b!=None and c!=None): #area of triangle use heros formula
            s=(a+b+c)/2
            ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
            print("Area of Triangle : ",ar)
        else:
            print("Invalid")
#main program
sh=shape()  #object of shape class
while(True):                  
    print("1. Area of Circle \n 2. Area of Rectangle \n 3. Area of Triangle \n 4. Exit")
    choice=int(input("Enter Your Choice : "))
    if(choice==1):
        r=int(input("Enter Radius : "))
        sh.area(r)
    elif (choice==2):
        l=int(input("Enter Length : "))
        w=int(input("Enter Width : "))
        sh.area(l,w)
    elif(choice==3):
        a=int(input("Enter sides of a : "))
        b=int(input("Enter sides of b : "))
        c=int(input("Enter sides of c : "))
        sh.area(a,b,c)
    elif(choice==4):
        break
    else:
        sh.area()
        print("invalid choice")
    
