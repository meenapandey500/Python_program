#method overriding 
#super class means base class
class polygon: #base class
    def number_of_sides(self):
        return 0
    def area(self):
        return 0
    def perimeter(self):
        return 0
#Derived class Triangle inherits from polygon base class
class Triangle(polygon):
    def number_of_sides(self):
        return 3
    def area(self,base,height):
        return 1/2*base*height
    def perimeter(self,a,b,c):
        return (a+b+c)/2
#Derived class Rhombus inherits from polygon base class
class Rhombus(polygon):
    def number_of_sides(self):
        return 4
    def area(self,a,b):
        return 1/2*a*b
    def perimeter(self,a):
        return 4*a
#Derived class Square inherits from polygon base class
class Square(polygon):
    def number_of_sides(self):
        return 4
    def area(self,a):
        return a*a
    def perimeter(self,a):
        return 4*a
#main program
#create the object of derived class Triangle
tri=Triangle()
print("No. of sides : ",tri.number_of_sides())
print("Area of triangle : ",tri.area(4,5))
print("Perimeter of triangle : ",tri.perimeter(4,5,7))
#create the object of derived class Rhombus
rh=Rhombus()
print("No. of sides : ",rh.number_of_sides())
print("Area of Rhombus : ",rh.area(4,5))
print("Perimeter of Rhombus : ",rh.perimeter(4))

#create the object of derived class Square
s=Square()
print("No. of sides : ",s.number_of_sides())
print("Area of Square : ",s.area(4))
print("Perimeter of Square: ",s.perimeter(4))


