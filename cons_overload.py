#example of constructor overloading 
#self is a reference type pointer variable
        #which hold the address of current object
class A: #here A user defined class
    def __init__(self,x=None): #constructor & parameter function(constructor overloading)
        if(x==None):              #None inbuilt
            self.x=9
        elif(x!=None):
            self.x=x
   
    def show(self):
        print("value of x : ",self.x)
    def __del__(self): #destructor constructor
        print("Clear memory")

#main program
A1=A() #default constructor
A2=A(14) #call parameter constructor
A1.show()
A2.show()
del A1  #call destructor
del A2
