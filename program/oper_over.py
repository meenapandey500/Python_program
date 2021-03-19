#example of operator overloading
class addition:
    def __init__(self,a): #parameter constructor function
        self.a=a
    def __add__(self,other): #other : object  obj1.a.__add__(obj2.a)
        return self.a+other.a
    def __gt__(self,other):
        if(self.a>other.a):
            return self.a
        else:
            return other.a
    def __mul__(self,other):
        f=1
        while(self.a>0):
            f=f*self.a
            self.a=self.a-1
        return f
    
#main program
a,b=[int(x) for x in input("Enter Two nos. separated by space : ").split()]
obj1=addition(a)
obj2=addition(b)
c=obj1+obj2
print("sum : ",c)
print("Greatest no. ",obj1>obj2)
print("Factorial : =",obj1*obj2)
