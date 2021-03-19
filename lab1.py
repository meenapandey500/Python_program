#WAP to find the area of triangle when given base and height
#using lambda function
area=lambda b,h:b*h/2

#main program
b,h=[int(x) for x in input("Enter base and height separated by space : ").split()]
print("Area of triangle : ",area(b,h))
