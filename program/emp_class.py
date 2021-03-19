class Employee: #Employee user defined class name
    def getdata(self):
      self.__empid=int(input("Enter Employee Id : "))
      self.__empname=input("Enter Employee name : ")
      self.__salary=float(input("Enter salary : "))
    def display(self):
        print("Empid : ",self.__empid)
        print("EmpName : ",self.__empname)
        print("EmpAddress  : ",self.__salary)
        
#main program
faculty=Employee()  #here faculty object name of Employee class
print("Enter Faculty Details : ")
faculty.getdata()
print("Faculty Details : ")
faculty.display()

clerk=Employee()
print("Enter Clerk Details : ")
clerk.getdata()
print("Print Clerk Details : ")
clerk.display()


