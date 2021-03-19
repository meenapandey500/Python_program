from connect import Connection # connect file connect.py  and class Connection
class Data_Manipulation:
    def insert_record(self):
        #create object of class Connection
        con1=Connection()
        con=con1.conn()
        #create cursor means create object of cursor
        cur=con.cursor()

        #query fire of insert means to insert record into table Employee table
        q="insert into Employee values(%s,%s,%s,%s,%s)"
        
        #input from user
        eid=int(input("Enter Employee Id : "))
        n=input("Enter Employee Name ")  #varchar type in table=string
        a=int(input("Enter Employee Age : "))
        m=input("Enter Employee Mobile No.  :")
        s=int(input("Enter Employee Salary :"))
        #create tuple
        val=(eid,n,a,m,s)
        #Insert Query run
        try:
            cur.execute(q,val)
        except:
            print("Query Error")
        else:
        #save in database  use commit()
            con.commit()
            print("Record Insert Successfully")
        #close connection
            cur.close()
            con.close()

    def menu(self):
        print("\n 1. Insert Record \n 2. View All Records \n 3. Search Record According Empid ")
        print("\n 4. Update Employee Salary \n 5.Update Employee Mobile \n 6. Delete Employee \n 7. Exit" )

    def View_Record(self):
        #create object of class Connection
        con1=Connection()
        con=con1.conn()
                 #Fire Select Query
        query="SELECT * FROM Employee"
                    #prepared cursor
        cur=con.cursor()
                    #run select query
        cur.execute(query)
        result=cur.fetchall()  #fetchone() to display only first record
        print(result)
        cur.close()
        con.close()
    def Search_Record(self):
        eid=int(input("Enter employee id no. to be Searched : "))
        #create object of class Connection
        con1=Connection()
        con=con1.conn()
                 #Fire Select Query
        query="SELECT * FROM Employee where Empid=%s"
                    #prepared cursor
        cur=con.cursor()
                    #run select query
        cur.execute(query,eid)
        result=cur.fetchall()  #fetchone() to display only first record
        print(result)
        cur.close()
        con.close()
    def update_Salary(self):
        con1=Connection()
        con=con1.conn()
        eid=int(input("Enter employee id no. to be updated : "))
        s=int(input("Enter Increment salary of Employee : "))
        #Fire delete Query
        query="UPDATE Employee SET Salary=%s WHERE Empid=%s"
        #prepared cursor
         #create object of class Connection
        
        cur=con.cursor() #to keep cursor on particular path
        q="SELECT Salary FROM Employee where Empid=%s"
        cur.execute(q,eid)
        result=cur.fetchall()
        sal=result[0]
        #print(sal)
        #print(type(sal))
        s1=sal[0]
        print("Current Salary " ,s1)
        s1=s1+s1*s/100
        print("After Increment , New Salary =",s1)
        val=(s1,eid)
        
        
        #run update query
        try:
            cur.execute(query,val)
            con.commit() #to changes permanently in table
            print(" Record Update  successfully")
        except:
            print("Record not found")
            cur.close()

    def delete(self):
        con1=Connection()
        con=con1.conn()
        eid=int(input("Enter Employee id no. to be deleted : "))
        #Fire delete Query
        query="delete FROM Employee WHERE Empid=%s"
        #prepared cursor
        cur=con.cursor()
        #run delete query
        try:
            cur.execute(query,eid)
            self.con.commit() #to changes permanently in table
            print("Delete Record successfully")
        except:
            print("Record not found")
        cur.close()
        con.close()
        

