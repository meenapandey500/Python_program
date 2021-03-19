#method overloading
#Find the area of triangle(a,b,c),rectangle(a,b) and circle(a)
from math import sqrt
class shape:
    def area(self,a=None,b=None,c=None):
        if(a!=None and b==None and c==None):  #Area of circle
            ar=3.14*a*a
            print("Area of circle=",ar)
        elif(a!=None and b!=None and c==None): #area of rectangle
            ar=a*b
            print("Area of Rectangle=",ar)
        elif(a!=None and b!=None and c!=None): #area of triangle(hero's formula
            s=(a+b+c)/2
            ar=sqrt(s*(s-a)*(s-b)*(s-c))
            print("Area of Triangle=",ar)
        else:
            print("Invalid ")

        
#main program
#create object of class shape
s=shape()
r=4
s.area(r)
s.area(5,6)
s.area(6,7,8)
s.area()
