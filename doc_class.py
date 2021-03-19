#example of single inheritance 
#class attributes : -
'''1. __doc__   :  its show documantation of class ,its call classname.__doc__ in main program
   2.__dict__  : its show dictionary of class
   3. __name__  :
'''
class Arithmetic: #base class
    "WAP to create a mini calculator "   #call with the help of __doc__ with classname.
    def __init__(self,a,b): #parameter constructor
        self._a=a  #here self._a  : protected variable
        self._b=b  #here self._b  : protected variable
    def show(self):
        print("value of a : ",self._a)
        print("value of b : ",self._b)
class calculator(Arithmetic):
    "here calculator derived class which inherits base class Arithmetic"
    def __init__(self,a,b): #constructor function
        super().__init__(a,b) #call constructor function of base class
    def sum(self):
        return (self._a+self._b)
    def subtract(self):
        return (self._a-self._b)
#main program
#create object of calculator derived class
print(Arithmetic.__doc__)
print(calculator.__doc__)
a=int(input("Enter number a  : "))
b=int(input("Enter number b  : "))
cal=calculator(a,b)
cal.show()
print("sum : ",cal.sum())
print("subtract : ",cal.subtract())
print(calculator.__dict__)
print(Arithmetic.__dict__)
print(calculator.__bases__) #show base class name of derived class calculator



