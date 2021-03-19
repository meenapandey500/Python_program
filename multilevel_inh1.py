#example of multiLevel inheritance
class A: #base class
    def __init__(self):
        self.__x=int(input("Enter No. x : "))
    def show_x(self):
        print("X=",self.__x)
        
class B(A) : #here B derived class ans inherits base class A
    def __init__(self):
        super().__init__() #call constructor of base class A
        self.__y=int(input("Enter No. y : "))
    def show_y(self):
        print("Y=",self.__y)

class C(B) : #here C derived class ans inherits base class B
    def __init__(self): #constructor function
        super().__init__() #call constructor of base class B
        self.__z=int(input("Enter No. z : "))
    def show_z(self):
        print("Z=",self.__z)
    def __del__(self): #destructor function
        print("Clear memory")
        
#main program
C1=C() #create object of derived class C
C1.show_x() #call
C1.show_y() #call
C1.show_z() #call
del C1 #call destructor function
C1=C()
C1.show_z()
