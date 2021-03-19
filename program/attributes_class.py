#class attributes
#1. __doc__  : inbuilt attributes of class ,to display documents of class
#__dict__  : inbuilt attributes of class , to shoa all description of class
#classname.__doc__
class addition:
    "Write a program to create a class , to fidn the sum of 2 nos."  #document
    def __init__(self):
        self.a=10
        self.b=20
    def sum(self):
        c=self.a+self.b
        print("sum : ",c)
#main program
print(addition.__doc__)
print(addition.__dict__) #distionary show
ad=addition()
ad.sum() #call
print("Class name : ",__name__)

