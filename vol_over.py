#Example of method overloading
#WAP to create volume of cube and cuboid
class shape :  #shape user defined class name
    def volume(self,a=None,b=None,c=None):
        if(a!=None and b==None and c==None):
            return a*a*a  #a**3   #volume of cube
        elif(a!=None and b!=None and c!=None): #volume of cuboid
            return a*b*c
        else:
            return "Invalid"
    def menu(self):
        print("\n 1. volume of cube \n 2. Volume of cuboid \n 3. invalid")

#main program
s=shape()  #create object of class shape
v=s.volume() #call
print(v)
s.menu()
ch=int(input("Enter your choice : "))
if(ch==1):
    side=int(input("enter side of cube : "))
    v=s.volume(side)#call method
    print("Volume of Cube : ",v)
elif(ch==2):
    side1=int(input("enter side1 of cuboid : "))
    side2=int(input("enter side2 of cuboid : "))
    side3=int(input("enter side3 of cuboid : "))
    v=s.volume(side1,side2,side3)
    print("Volume of Cuboid : ",v)
else:
    print("Invalid choice : ")
