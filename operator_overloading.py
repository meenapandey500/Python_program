#example of operator overloading __add__(self,object)
class A:
    def __init__(self,x): #constructor function
        self.x=x
    #adding two objects
    def __add__(self,other):
        return self.x+other.x

#main program
x=int(input("Enter first no. x : "))
y=int(input("Enter second no. : "))
#create object of class
ob1=A(x) #create first object of class A
ob2=A(y) #create second object of class A
print("sum of 2 nos : ", ob1+ob2)
x="meena"
y="pandey"
ob3=A(x)
ob4=A(y)
print("Full Name : ",ob3+ob4)
