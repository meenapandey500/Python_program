class Employee:
    def getdata(self): #self instance variable
        self.Emp_no=101  #public variable
        self.Emp_name="Meena Pandey" #public variable
        self.Salary=67000 #public variable
    def display(self):
        print("Emp no :",self.Emp_no)
        print("Emp Name : ",self.Emp_name)
        print("Salary : ",self.Salary)

#main program
Sales=Employee()
Sales.getdata() #call
Sales.display() #call
#update Salary with 90000
Sales.Salary=90000
print("After Update Salary : ")
Sales.display()
