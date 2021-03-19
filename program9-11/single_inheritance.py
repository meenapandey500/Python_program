#example of single inheritance
class student :   #student base class
    def __init__(self): #constructor function
        self.__rno=int(input("Enter Rollno. : "))
        self.__name=input("Enter Name : ")
        self.__age=int(input("Enter age : "))
        self.__city=input("Enter City : ")
    def display(self):
        print("Roll no. : ",self.__rno)
        print("Name : ",self.__name)
        print("Age : ",self.__age)
        print("City : ",self.__city)
class marks(student):  #derived class student inherits base class student
    def __init__(self):  #constructor
        super().__init__() #call constructor function of base class student
        self.__phy=float(input("Enter marks of physics : "))
        self.__chem=float(input("Enter marks of chemistry : "))
        self.__maths=float(input("Enter marks of maths : "))
        self.__eng=float(input("Enter marks of English : "))
    def display(self):
        student.display(self) #call display() of base class
        print("Marks in Physics : ",self.__phy)
        print("Marks in Chemistry : ",self.__chem)
        print("Marks in Maths : ",self.__maths)
        print("Marks in HIndi : ",self.__eng)
#main program
#create object of derived class marks
m=marks()
m.display()

