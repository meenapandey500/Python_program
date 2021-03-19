class shape:
   ''' def area(self,r):
        return 3.14*r*r
    def area(self,l,w):
        return l*w'''
   def area(self,a=None,b=None):
       if(a!=None and b==None):
           return 3.14*a*a
        elif(a!=None and b!=None):
            return a*b
        else:
            return "invalid"
#main program
#create object of class
s=shape()
print("Area of circle : ",s.area(3))
print("area of rectangle " , s.area(4,5))

