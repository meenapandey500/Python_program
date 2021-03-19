from connect import Connection # connect file connect.py  and class Connection
class Data_Manipulation:
    def insert_record(self):
        #create object of class Connection
        con=Connection()
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
