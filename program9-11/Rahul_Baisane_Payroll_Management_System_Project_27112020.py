'''First created payroll database and employee table, in table created column name in sequence like (id,name,designation,basic_salary,da,hra,gross_salary,tax,net_salary  '''

print("    ------Project Title------     ")
print("------Payroll Management System------")
input() #to hold the output screen
print(" *****Created by Rahul Baisane***** ")
print("-Using Python Programming Language-")
input() #to hold the output screen

import pymysql #To create a connection string (between python and mysqlserver)
import datetime #used for current date and time
from tabulate import tabulate #used for get the data in the form of table

servername="localhost"
username="root"
password=""
dbname="payroll"
try:
    con=pymysql.connect(servername,username,password,dbname)
except:
    print("Mysql server Connectivity Error")
else:
    print("Mysql server Connect Successfully.")
#main program
while(True):
    print("\n*****Payroll Management System: Main Menu*****")
    print("\t\t\t\t1. Add Employee Details")
    print("\t\t\t\t2. Display record of all the Employee")
    print("\t\t\t\t3. Display record of a particular Employee")
    print("\t\t\t\t4. Delete record of all the Employee")
    print("\t\t\t\t5. Delete record of a particular Employee")
    print("\t\t\t\t6. Modification of Employee Details")
    print("\t\t\t\t7. Display Payroll")
    print("\t\t\t\t8. Display salary slip of all the Employee")
    print("\t\t\t\t9. Display salary slip of a particular Employee")
    print("\t\t\t\t10. Exit")
    print("Enter Choice: ",end="") 
    choice=int(input())
    if choice==1:
        try: #use try
            print("Enter Employee Details: ")
            emp_id=int(input("Enter Employee Id: "))
            emp_name=input("Enter Empoyee Name: ")
            emp_designation=input("Enter Employee Designation: ")
            emp_basicsalary=float(input("Enter Empoyee Basic Salary: "))
            if(emp_basicsalary<20000):
                da=emp_basicsalary*0.5
                hra=emp_basicsalary*0.35
                tax=emp_basicsalary*0.2
            else:
                da=emp_basicsalary*0.45
                hra=emp_basicsalary*0.30
                tax=emp_basicsalary*0.15
            emp_grosssalary=emp_basicsalary+da+hra
            emp_netsalary=emp_grosssalary-tax
            query="INSERT INTO EMPLOYEE(id,name,designation,basic_salary,da,hra,gross_salary,tax,net_salary)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(emp_id,emp_name,emp_designation,emp_basicsalary,da,hra,emp_grosssalary,tax,emp_netsalary) #val tuple variable
            #Prepare cursor
            cur=con.cursor()
            #Run insert query
            try:
                cur.execute(query,val)
            except:
                print("Query Error")
            else:
                con.commit() #Save in database used commit()
                print("Employee details Insert Successfully")
        except:
            print("Something went Wrong")
    elif choice==2:
        try:
            #Fire select query
            query="SELECT * FROM EMPLOYEE"
            #Prepare cursor
            cur=con.cursor()
            #Run select query
            cur.execute(query)
            #Print query
            print(tabulate(cur,headers=['Id','Name','Designation','Basic Salary','DA','HRA','Gross Salary','Tax','Net Salary'],tablefmt='fancy_grid'))
        except:
            print("Something Went Wrong")
    elif choice==3:
        try:
            e_id=input("Enter Employee Id of the record to be Displayed: ")
            #Fire select query
            query="SELECT * FROM EMPLOYEE WHERE id="+e_id
            #Prepare cursor
            cur=con.cursor()
            #Run select query
            cur.execute(query)
            print(tabulate(cur,headers=['Id','Name','Designation','Basic Salary','DA','HRA','Gross Salary','Tax','Net Salary'],tablefmt='fancy_grid'))
            result=cur.fetchone()
            print("\n\nRecord of Employee Id: ",e_id)
            print(result)
            c=cur.rowcount
            if c==-1:
                print("Nothing to Display")
        except:
            print("Something Went Wrong")
    elif choice==4:
        try:
            ch=input("Do  you want to delete all the Employee Record (y/n): ")
            if ch.upper()=="Y":
                cur.execute("delete from" +employee)
                con.commit()
                print("All the Records are deleted")
        except:
            print("Something Went Wrong")
    elif choice==5:
        try:
            e_id=input("Enter Employee Id of the record to be Deleted: ")
            query="DELETE FROM employee where id="+e_id
            cur.execute(query)
            con.commit()
            c=cur.rowcount
            if c>0:
                print("Deletion Done")
            else:
                print("Employee Id ",e_id," not found")
        except:
             print("Something went wrong")
    elif choice==6:
        try:
            e_id=input("Enter Employee Id of the record to be modified: ")
            query="SELECT * FROM employee where id="+e_id
            cur.execute(query)
            result=cur.fetchall()
            c=cur.rowcount
            if c==-1:
                print("Enter Id does not exist: ",e_id)
            else:
                mname=result[1]
                mdesignation=result[2]
                mbasic_salary=result[3]
                print("Id: ",result[0])
                print("Name: ",result[1])
                print("Designation: ",result[2])
                print("Basic Salary: ",result[3])
                print("DA: ",result[4])
                print("HRA: ",result[5])
                print("Gross Salary: ",result[6])
                print("Tax: ",result[7])
                print("Net Salary: ",result[8])
                print("--------------------------")
                print("Type  value to be modify below or just press Enter for no change")
                x=input("Enter Name: ")
                if len(x)>0:
                    mname=x
                x=input("Enter Designation: ")
                if len(x)>0:
                    mdesignation=x
                x=input("Enter Basic Salary: ")
                if len(x)>0:
                    mbasic_salary=float(x)
                query='update '+employee+' set name='+"'"+mname+"'"+','+'designation='+"'"+mdesignation+"'"+','+'basicsalary='+\
                       "'"+str(mbasic_salary)+' where id='+e_id
                print(query)
                cur.execute(query)
                con.commit()
                print("Records are successfully modified")
        except:
            print("aaaSomething went wrong")
    elif choice==7:
        try:
            query="SELECT * FROM EMPLOYEE"
            cur.execute(query)
            result=cur.fetchall()
            print("\n\n\n")
            print(95*'*')
            print("Employee Payroll".center(90))
            print(95*'*')
            now=datetime.datetime.now()
            print("Current Date and Time: ",end=' ')
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print()
            print(95*'-')
            print('%-5s %-15s %-10s %-8s %-8s %-8s %-9s %-8s %-9s'\
                      %("Id","Name","Designation","Basic Salary","DA","HRA","Gross Salary","Tax","Net Salary"))
            print(95*'-')
            for rec in result:
                print('%4d %15s %10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
            print(95*'-')      
        except:
            print("Something went wrong")
    elif choice==8:
        try:
            query="SELECT * FROM EMPLOYEE"
            cur.execute(query)
            tym=datetime.datetime.now()
            print("\n\n\n")
            print("-"*95)
            print("\t\t\t\tSalary Slip")
            print("-"*95)
            print("Current Date and Time: ",end=" ")
            print(tym.strftime("%Y-%m-%d %H:%M:%S"))
            result=cur.fetchall()
            for rec in result:
                print("%4d %-15s %10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f" %rec)
        except:
            print("Something went wrong")
    elif choice==9:
        try:
            e_id=input("Enter employee id whose pay slip you want to retrieve: ")
            #query="SELECT * FROM "+employee+" where id="+e_id
            query="SELECT * FROM EMPLOYEE WHERE ID="+e_id
            cur.execute(query)
            now=datetime.datetime.now()
            print("\n\n\n\t\t\tSALARY SLIP")
            print("Current Date and Time: ",end=" ")
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            #Print(query)
            print(tabulate(cur,headers=['Id','Name','Designation','Basic Salary','DA','HRA','Gross Salary','Tax','Net Salary'],tablefmt='fancy_grid'))
        except:
            print("Something went wrong")
    elif choice==10:
        break
    else:
        print("Wrong Choice")






                
        
