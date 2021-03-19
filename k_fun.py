#passing argument and return value
#B) Keyword  argument
#for example
#WAP to find the area of triangle when given base and height user defined function

def area(b,h):
    print("Base : ",b)
    print("Height : ",h)
    return b*h/2

#main program
x=int(input("Enter Base  : "))
y=float(input("Enter Height : "))
#call function
ar=area(h=y,b=x)
print("Area of Triangle : ",ar)
