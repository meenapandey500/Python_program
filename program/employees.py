class Employee:
    def getdata(self): #getdata( ) user defined function
        #self is a instance variable means address of object
        self.empid=input("Enter Employee Id ")  #empid local variable
        self.Ename=input("Enter Employee Name : ")
        self.age=int(input("Enter age : "))
        self.salary=float(input("Enter Salary : "))
        self.mobile=int(input("Enter Mobile no. :"))
        self.pre_cname=input("Enter Previous company name")
        self.email=input("Enter Email address : ")

    def display(self): #display() user defined function
        print("Employee Id : ",self.empid)
        print("Employee Name : ",self.Ename)
        print("Age : ",self.age)
        print("Salary : ",self.salary)
        print("Mobile : ",self.mobile)
        print("Previous company : ",self.pre_cname)
        print("Email : ",self.email)
        
