#Write a program to create the following menu driven program
'''1. Volume of sphere  formula : v=4/3*pi*r^3  where r means radius and pi=3.14 or 22/7 (constant)
   2. Volume of Cube  v=a*a*a where a=sides
   3. Perimeter of rectangle  perimeter=2(l+b) where l=length and b=breadth'''

print("1. Volume of sphere \n2. Volume of Cube \n3. Perimeter of rectangle") # \n means inbuilt command for new line
ch=int(input("Enter Your choice : "))
if(ch==1):
    r=float(input("Enter radius of sphere : "))
    v=4/3*3.14*(r**3)
    print("Volume of sphere : ",round(v,1)) #round(variablename,after decimal digit) 
elif(ch==2):
    a=float(input("Enter sides of cube : "))
    v=a**3
    print("Volume of cube : ",v)
elif(ch==3):
    l=float(input("Enter Length of rectangle : "))
    w=float(input("Enter width of rectangle : "))
    p=2*(l+w)
    print("Perimeter of rectangle : ",p)
else:
    print("Invalid choice ")
