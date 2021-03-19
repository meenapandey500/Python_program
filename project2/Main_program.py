from Employee_module import Employee
from connect1 import Connection
class User:
    def Admin_user(self):
        u=input("Enter Admin's User Id : ")
        p=input("Enter Admin's Passowrd : ")
        if(u=="Admin" and p=="Admin"):
            return True
        else:
            return False
    def Employee_user(self):
        u=input("Enter Employee's User Id : ")
        p=input("Enter Employee's Password : ")
        query="select * from emp_login where Empid=%s and Password=%s"
        #create object of class Connection
        cn=Connection() #cn user defined object of Connection class
        msg,con=cn.show()
        print(msg)
        #print(con)
        #create cursor
        cur=con.cursor()
        val=(u,p)
        #Query run
        cur.execute(query,val)
        result=cur.fetchall()
        try:
            if(u==result[0][0] and p==result[0][1]):
                query="select * from Employee where Empid=%s"
        #create object of class Connection
                cn=Connection() #cn user defined object of Connection class
                msg,con=cn.show()
                print(msg)
                #print(con)
                #create cursor
                cur=con.cursor()
                #Query run
                cur.execute(query,u)
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
            else:
                raise Exception("invalid userid and password")
        except Exception as e:
            print(e)
    def menu(self):
        print("1. Admin \n 2. Employee \n3. Exit ")
#main program
#create object of Admin
u=User()
while(True):
    u.menu()
    ch=int(input("Enter Your choice : "))
    if(ch==1):
        ans=u.Admin_user()
        if(ans==True):
            #create object of employee class
            emp=Employee()
            while(True):
                emp.menu()
                ch=int(input("Enter Your choice : "))
                if(ch==1):
                   emp.add_new_employee()
                elif(ch==2):
                    emp.view_all_employees()
                elif(ch==3):
                    emp.Search_particular_employees()
                elif(ch==4):
                    emp.Delete_particular_employees()   
                elif(ch==5):
                   break
        else:
            print("Invalid Admin userid and password: ")

    elif(ch==2):
        u.Employee_user()
    elif(ch==3):
        break
    else:
        print("Invalid Choice ")
            
