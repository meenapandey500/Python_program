class Employee:
    def __init__(self): #__init__() constructor function : it is call automatic in main
        #or anywhere when create the object of class in main program or anywhere
        self.__Emp_no=101  #private variable
        self.__Emp_name="Meena Pandey" #private variable
        self.__Salary=67000 #private variable
    def display(self):
        print("Emp no :",self.__Emp_no)
        print("Emp Name : ",self.__Emp_name)
        print("Salary : ",self.__Salary)

    def __del__(self): #destructor function
        print("Clear memory of object")
#main program
Sales=Employee()

Sales.display() #call
del(Sales) #call destructor function

