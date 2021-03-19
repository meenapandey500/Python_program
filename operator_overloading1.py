#example of operator overloading __gt__(self,object)
class A:
    "Greatest of 2 nos. using operator overloading __dt__(selt,other)"
    def __init__(self,x): #constructor function
        self.x=x
    #adding two objects
    def __gt__(self,other):  #gt greater than
        if(self.x>other.x):
            return self.x
        else:
            return other.x
    def __del__(self):
        print("Clear memory")
#main program
print(A.__doc__) #show document classname.__doc__
print("class name : ",A.__name__)
x=int(input("Enter first no. x : "))
y=int(input("Enter second no. : "))
#create object of class
ob1=A(x) #create first object of class A
ob2=A(y) #create second object of class A
print("Greatest no. = ",ob1>ob2)
print("Dictionary of class : ",A.__dict__) #to show all dictionary of our class

#call destructor function
del ob1
del ob2
