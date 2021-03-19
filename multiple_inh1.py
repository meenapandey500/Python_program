#example of multiple inheritance
class A: #base class-1
    def __init__(self): #constructor function
        self._x=int(input("Enter No. x : ")) #here _x protected variable
    def show_x(self):
        print("X=",self._x)
        
class B: #base class-2
    def __init__(self): #constructor function
        self._y=int(input("Enter No. y : ")) #here _y protected variable
    def show_y(self):
        print("Y=",self._y)

class C : #base class-3
    def __init__(self): #constructor function
        self._z=int(input("Enter No. z : ")) #here _z protected variable
    def show_z(self):
        print("Z=",self._z)

class D(A,B,C): #here D derived class and inherits the features of base class A,B,and C
    def __init__(self): #constructor function
        super().__init__() #call constructor of base class
        B.__init__(self)
        C.__init__(self) #if call constructor name with class name then use self 
    def compute(self):
        self.result=self._x+self._y+self._z
        print("Sum of 3 nos. : ",self.result)
    def __del__(self): #destructor function
        print("Clear memory")
        
#main program
D1=D() #create object of derived class D
D1.show_x() #call
D1.show_y() #call
D1.show_z() #call
D1.compute()
del D1 #call destructor function'''

