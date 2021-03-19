#Example of operator Overloading
class arithmetic:
    def __init__(self,a): #parameter constructor
        self.a=a
    def __add__(self,other): #self : object and other : object
        return self.a*other.a
    def __mul__(self,other): #find the factorial
        ans=1
        while(self.a>0):
            ans=ans*self.a
            self.a=self.a-1
        return ans
        
        
#main program
ar1=arithmetic(5)
ar2=arithmetic(40)

#call function
c=ar1+ar2
print("Multiply : ",c)
#call
result=ar1*ar2
print("Factorial : ",result)
