class Employee:
    def getdata(self): #self instance variable
        self.__Emp_no=101  #private variable
        self.__Emp_name="Meena Pandey" #private variable
        self.__Salary=67000 #private variable
    def display(self):
        print("Emp no :",self.__Emp_no)
        print("Emp Name : ",self.__Emp_name)
        print("Salary : ",self.__Salary)

#main program
Sales=Employee()
Sales.getdata() #call
Sales.display() #call
#update Salary with 90000
Sales.__Salary=90000
print("After Update Salary : ")
Sales.display()
print("salary : ",Employee.__Salary)
