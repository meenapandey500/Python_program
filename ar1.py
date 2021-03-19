#WAP to find the area of triangle when given 3 sides a,b,c
from math import sqrt
a=float(input("Enter side a of triangle : "))
b=float(input("Enter side b of triangle : "))
c=float(input("Enter side c of triangle : "))
#find the perimeter s
s=(a+b+c)/2

#BODMAS RULE : precedance of operator :
#B : bracket O :open  D : divide M : Multiply  A : addition  S : subtraction
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle : ",round(area,2))
