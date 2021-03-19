'''Create a class Number with a private variable __num initialised through the constructor.
Write methods increment, decrement and display. Create multiple objects from it. '''
class Number:
    def __init__(self): #constructor function
        self.__num =5 #initialised value suppose assign __num=5
    def display(self):
        print("Number : ",self.__num)
    
    def increment(self):
        self.__num=self.__num+1 #self.__num+=1
    def decrement(self):
        self.__num=self.__num-1 #self.__num-=1
    def __del__(self): #destructor function 
        print("Clear Memory ")
#main program

n1=Number() #create object of NUmber() class
n1.display()  #5
n1.increment()
print("After Increment : ")
n1.display() #6
n1.decrement() #call
print("After Decrement : ")
n1.display() #5
n2=Number()#create object of NUmber() class
n2.display()  #5
n2.increment()
print("After Increment : ")
n2.display() #6
n2.decrement() #call
print("After Decrement : ")
n2.display() #5
del(n1)
del(n2)
