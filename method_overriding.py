#example of method overriding
class polygon: #base class
    def no_of_sides(self):
        pass  #no defination
    def area(self):
        pass
    def perimeter(self):
        pass
class triangle(polygon): #here triangle derived class inherits base class polygon
    def no_of_sides(self):
        return 3
    def area(self):
        base=int(input("Enter base of triangle : "))
        h=int(input("Enter height of triangle : "))
        return base*h/2
    def perimeter(self):
        a=int(input("Enter sides of a : "))
        b=int(input("Enter sides of b : "))
        c=int(input("Enter sides of c : "))
        s=(a+b+c)/2
        return s
class square(polygon): #here square derived class inherits base class polygon
    def no_of_sides(self):
        return 4
    def area(self):
        side=int(input("Enter side of square : "))
        return side*side
    def perimeter(self):
        side=int(input("Enter side of square : "))
        return 4*side

#main program
tr=triangle()    #tr is a user defined object of triangle class
print("No. of sides of triangle : ",tr.no_of_sides())
print("Area of triangle : ",tr.area())
print("Perimeter of trianlge : ",tr.perimeter())

sq=square() #sq user defined object of square derived class
print("No. of sides of square : ",sq.no_of_sides())
print("Area of square : ",sq.area())
print("Perimeter of square : ",sq.perimeter())


        
