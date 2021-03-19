#create class Employee
class Employee :  #Employee user defined class name
    def getdata(self): #user defined function
        self.empid=int(input("enter Employee Id :"))
        self.empname=input("Enter Employee Name : ")
        self.mobile=int(input("Enter Mobile No. : "))
        self.salary=float(input("Enter Basic Salary : "))
    def display(self):
        print("Employee Id : ",self.empid)
        print("Employee Name : ",self.empname)   
        print("Employee's Salary : ",self.salary)
        print("Employee's mobile :",self.mobile)

#main program
sales=Employee()  #sales is a user defined object of Employee
sales.getdata()
print("Details of Sales's Employees")
sales.display()

trainer=Employee() #trainer is a user defined object of Employee
trainer.getdata()
print("Details of Trainer :")
trainer.display()
