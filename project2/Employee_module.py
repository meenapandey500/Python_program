#Create Admin Module : -
from connect1 import Connection
#from filename import classname
class Employee:
    def add_new_employee(self):
        eid=input("Enter Employee Id : ")
        p=input("enter Password : ")
        ename=input("Enter employee Name : ")
        dob=input("enter Date of Birth yyyy-mm-dd ")
        doj=input("enter Date of Joining yyyy-mm-dd ")
        mob=input("enter Mobile Number : ")
        em=input("enter Email Address : ")
        s=int(input("enter Salary : "))
        #to insert all values of employees in Employee table
        query1="insert into Emp_Login values(%s,%s)"
        query2="insert into Employee values(%s,%s,%s,%s,%s,%s,%s)"

        #path the table then create connectionstring which define in Connection class :- this
        #class save in connect1,py file so call this file connect1
        #create object of class Connection
        cn=Connection() #cn user defined object of Connection class
        msg,con=cn.show()
        print(msg)
        #print(con)
        #create cursor
        cur=con.cursor()
        #tuple create
        val1=(eid,p)
        val2=(eid,ename,dob,doj,mob,em,s)
        #query run
        try:
            cur.execute(query1,val1)
        except Exception:
            print("Query1 Error")
        else:
            print("Login create successfully")
            con.commit() #record save permanently in table
            cur.close() #cursor close
        #create cursor
        cur=con.cursor()
        try:
            cur.execute(query2,val2)
        except Exception:
            print("Query2 Error")
        else:
            print("Employee's Record add successfully")
            con.commit() #record save permanently in table
            cur.close()
        del cn #call constructor function

    def view_all_employees(self):
        #to show all details of Employee
        query="select * from Employee"
        #create object of class Connection
        cn=Connection() #cn user defined object of Connection class
        msg,con=cn.show()
        print(msg)
        #print(con)
        #create cursor
        cur=con.cursor()
        #Query run
        cur.execute(query)
        result=cur.fetchall()
        print("********Employee's Details : ****** ")
        for row in result:
            print("\n")
            print("Employee Id : " ,row[0])
            print("Employee Name : " ,row[1])
            print("Employee's DOB : " ,row[2])
            print("Employee's DOJ : " ,row[3])
            print("Employee's Mobile : " ,row[4])
            print("Employee's Email : " ,row[5])
            print("Employee's Salary : " ,row[6])
            a=input("Press Enter to Next Record : ")
        cur.close()
        del cn #call constructor function
        
    def Search_particular_employees(self):
        eid=input("Enter Employee Id to be searched: ") 
        #to show  details of Particular Employee according to empid
        
        query="select * from Employee where Empid=%s"
        #create object of class Connection
        cn=Connection() #cn user defined object of Connection class
        msg,con=cn.show()
        print(msg)
        #print(con)
        #create cursor
        cur=con.cursor()
        #Query run
        cur.execute(query,eid)
        result=cur.fetchall()
        print("********Employee's Details : ****** ")
        for row in result:
            print("\n")
            print("Employee Id : " ,row[0])
            print("Employee Name : " ,row[1])
            print("Employee's DOB : " ,row[2])
            print("Employee's DOJ : " ,row[3])
            print("Employee's Mobile : " ,row[4])
            print("Employee's Email : " ,row[5])
            print("Employee's Salary : " ,row[6])
            a=input("Press Enter to Next Record : ")
        cur.close()
        del cn #call constructor function
    def Delete_particular_employees(self):
        eid=input("Enter Employee Id to be searched: ") 
        #to show  details of Particular Employee according to empid
        
        query="delete from Employee where Empid=%s"
        #create object of class Connection
        cn=Connection() #cn user defined object of Connection class
        msg,con=cn.show()
        print(msg)
        #print(con)
        #create cursor
        cur=con.cursor()
        #Query run
        try:
            cur.execute(query,eid)
        except Exception:
            print("Query Error")
        else:
            print("Employee's Record deleted successfully")
            con.commit() #Action permanently save in table
            cur.close()
            query1="delete from emp_login where Empid=%s"
            cur=con.cursor()
        #Query run
        try:
            cur.execute(query1,eid)
        except Exception:
            print("Query Error")
        else:
            print("Employee's Record deleted successfully")
            con.commit() #Action permanently save in table
            cur.close()
        del cn #call constructor function
    def menu(self):
        print("1. Add New Employees \n 2. View Records of all Employees")
        print("\n3. Search Employee in Empid\n 4. Delete Employee in Empid\n5. Exit")

        
