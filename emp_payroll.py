import pymysql
class emp_payroll:
    def __init__(self,empno,empname,age,basic_salary,mobile,desig):
        self.__eno=empno
        self.__en=empname
        self.__age=age
        self.__bs=basic_salary
        self.__mobile=mobile
        self.__desig=desig
        self.__conn=pymysql.connect(host='localhost',user='root',password='',database='itvedant')
        print("__connection sucessfully")
        self.cur=self.__conn.cursor()
        
    def insertrecord(self):
        q="insert into employee(emp_id,empname,age,bs,mobile,desig)values(%s, %s, %s, %s, %s, %s)"
        val=(self.__eno,self.__en,self.__age,self.__bs,self.__mobile,self.__desig)
        self.cur.execute(q,val)
        self.__conn.commit()
        print("record insert successfully",self.cur.rowcount)
    def displayrecord(self):
        q="select * from employee"
        self.cur.execute(q)
        records=self.cur.fetchall()
        for row in records:
            print("employee no. : ",row[0])
            print("employee name ",row[1])
            print("employee age : ",row[2])
            print("BAsic salary : ",row[3])
            print("mobile no. : ",row[4])
            print("designation : ",row[5])
    def searchrecord(self,empno):
        q="select * from employee where emp_id=%s"
        self.cur.execute(q,empno)
        records=self.cur.fetchall()
        for row in records:
            print("employee no. : ",row[0])
            print("employee name ",row[1])
            print("employee age : ",row[2])
            print("BAsic salary : ",row[3])
            print("mobile no. : ",row[4])
            print("designation : ",row[5])
            break
        else:
            print("employee no. does not exist")
    def deleterecord(self,empno):
           q="delete from employee where emp_id=%s"
           self.cur.execute(q,empno)
           self.__conn.commit()
           print("record delete successfully",self.cur.rowcount)
    def updaterecord(self,empno,new_desig):
        q="update employee set desig=%s where emp_id=%s"
        val=(new_desig,empno)
        self.cur.execute(q,val)
        self.__conn.commit()
        print("record update successfully",self.cur.rowcount)
    def __del__(self): #destructor function
            print("memeory clear")

#main program
x="y"
while(x=="y"):
    empno=int(input("enter empno"))
    empname=input("enter name of employee")
    age=int(input("enter age of employee"))
    basic_salary=float(input("enter basic salary"))
    mobile=input("enter mobileno.")
    desig=input("enter designation")
    e1=emp_payroll(empno,empname,age,basic_salary,mobile,desig)
    e1.insertrecord()
    x=input("add another records y/n")
ans=input("Show all records from table y/n")
if(ans=="y"):
    e1.displayrecord()
else:
    print("OK")
ans=input("search particular employee record y/n")
if(ans=="y"):
    empno=int(input("enter empno to be searched"))
    e1.searchrecord(empno)
else:
    print("ok")
ans=input("delete  particular employee record y/n")
if(ans=="y"):
    empno=int(input("enter empno to be deleted"))
    e1.deleterecord(empno)
else:
    print("ok")
ans=input("update particular employee record y/n")
if(ans=="y"):
    empno=int(input("enter empno to be update"))
    new_desig=input("enter new designation")
    e1.updaterecord(empno,new_desig)
else:
    print("ok")
del e1


        
        
        
        
        
    
