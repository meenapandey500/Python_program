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
        self._phy=float(input("Enter marks of physics : "))
        self._chem=float(input("Enter marks of chemistry : "))
        self._maths=float(input("Enter marks of maths : "))
        self._eng=float(input("Enter marks of English : "))
    def display(self):
        student.display(self) #call display() of base class
        print("Marks in Physics : ",self._phy)
        print("Marks in Chemistry : ",self._chem)
        print("Marks in Maths : ",self._maths)
        print("Marks in HIndi : ",self._eng)
class result(marks): #result derived class and inherits base class marks
    def __init__(self):
        super().__init__() #call constructor function of base class marks
    def compute(self):
        self.__total=self._phy+self._chem+self._maths+self._eng
        self.__percent=self.__total*100/400
    def display(self):
        marks.display(self) #call 
        print("Total Marks : ",self.__total)
        print("Percent : ",self.__percent)
#main program
#create object of derived class result
res=result()
res.compute()
res.display()

