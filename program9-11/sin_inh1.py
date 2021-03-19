class square:  #base class
    def __init__(self): #constructor function
        self.side=int(input("enter side : "))
    def area(self):
        return self.side*self.side
class cube(square): #here cube : derived class and inherits the features of base class square
    def area(self):
        return super().area()*6   #area of cube=6*side*side
    def volume(self):
        return super().area()*self.side          #volume of cube=side*side*side
#main program
#create object of derived class
c=cube()
ar=c.area()
v=c.volume()
print("Area of cube : ",ar)
print("Volume of cube : ",v)
