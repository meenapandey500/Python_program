#Example of Method Overriding (Hierarchical Inheritance)
class Polygon : #Polygon user defined base class
    def no_of_sides(self):
        return 0
    def area(self):
        return 0
    def perimeter(self):
        return 0

class Triangle(Polygon):
    #here Triangle derived class and inherits features of base class Polygon
    def no_of_sides(self):
        return 3
    def area(self,b,h):
        return b*h/2
    def perimeter(self,a,b,c):
         return (a+b+c)/2
class Square(Polygon):
     #here Square derived class and inherits features of base class Polygon
    def no_of_sides(self):
        return 4
    def area(self,a):
        return a*a
    def perimeter(self,a):
        return 4*a
class Rectangle(Polygon):
    #here Rectangle derived class and inherits features of base class Polygon
    def no_of_sides(self):
        return 2
    def area(self,l,w):
        return l*w
    def perimeter(self,l,w):
        return 2*(l+w)
    
#main program
while(True):
    print("\n 1. Triangle \n 2. Square \n 3. Rectangle \n 4. exit ")
    ch=int(input("Enter Your choice : "))
    if(ch==1):
        tr=Triangle() #create object of Triangle derived class
        print("No. of Sides : ",tr.no_of_sides())
        b=float(input("Enter Base of Triangle : "))
        h=float(input("Enter Height of Triangle : "))
        ar=tr.area(b,h)
        print("Area of Triangle : ",ar)
        a=float(input("Enter side of Triangle a : "))
        b=float(input("Enter side of Triangle b : "))
        c=float(input("Enter side of Triangle c : "))
        p=tr.perimeter(a,b,c)
        print("Perimeter of Triangle : ",p)
    elif(ch==2):
        sq=Square() #create object of Square derived class
        print("No. of Sides in Square: ",sq.no_of_sides())
        a=float(input("Enter side of square : "))
        ar=sq.area(a)
        print("Area of Square : ",ar)
        p=sq.perimeter(a)
        print("Perimeter of Square : ",p)
    elif(ch==3):
        rec=Rectangle() #create object of Rectangle derived class
        print("No. of Sides in Rectangle: ",rec.no_of_sides())
        l=float(input("Enter Length of Rectangle: "))
        w=float(input("Enter Width of Rectangle: "))
        ar=rec.area(l,w)
        print("Area of Rectangle : ",ar)
        p=rec.perimeter(l,w)
        print("Perimeter of Rectangle : ",p)
    elif(ch==4):
        break #exit from loop
    else:
        print("\n Invalid choice")



    
