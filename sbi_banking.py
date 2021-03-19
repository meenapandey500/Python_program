import pymysql
import login
#class create
class Bank:
    def __init__(self): #constructor function
        # Step 1 :  #Create a connection string between python and mysqlserver
        __servername="localhost"  #private declare
        __username="root" #private declare
        __password="" #private declare
        __dbname="SBI_Bank" #database name , #private declare

        try:
            self.__con=pymysql.connect(__servername,__username,__password,__dbname)
        # con user defined object (object means collection of data)
        except Exception:
           print("Connection Error")
        else:
            print("Connection successfully created")

    def __del__(self): #destructor function
        self.__con.close()  #connection close

    def insertrecord(self):
        cur=self.__con.cursor()
        query="INSERT INTO customer(custid,custname,address,mobile,city)VALUES(%s,%s,%s,%s,%s)"
        cid=int(input("Enter Customer Id : "))
        cname=input("Enter Customer Name : ")
        addr=input("enter Address of customer : ")
        c=input("enter City of Customer : ")
        m=input("Enter Mobile No. : ")
        
        #create tuple (immutable)
        val=(cid,cname,addr,m,c)
        try:
            cur.execute(query,val) #Query run
        except Exception:
            print("Query Error")
        else:
            print("Record Insert successfully in table")
            self.__con.commit()
            cur.close()

    def selectallrecord(self):
        cur=self.__con.cursor() #to connect the table into connection string
        query="SELECT * FROM customer" #* means all fields
        try:
            cur.execute(query)
        except Exception:
            print("Query Error")
        else:
            result=cur.fetchall()
            print(result)
            cur.close()

    def select_particular_record(self):
        print("1. Customer Id ")
        print("2. Customer Name ")
        print("3. Mobile No.")
        print("4. City ")
        ch=int(input("Enter Your choice : "))
        if(ch==1):
            cid=int(input("Enter Customer Id to be searched : "))
            cur=self.__con.cursor() #to connect the table into connection string
            query="SELECT * FROM customer where custid=%s" 
            try:
                cur.execute(query,cid)
            except Exception:
                print("Query Error")
            else:
                result=cur.fetchall()
                print(result)
                cur.close()
        elif(ch==2):
            cname=input("Enter Customer name to be searched : ")
            cur=self.__con.cursor() #to connect the table into connection string
            query="SELECT * FROM customer where custname=%s" 
            try:
                cur.execute(query,cname)
            except Exception:
                print("Query Error")
            else:
                result=cur.fetchall()
                print(result)
                cur.close()
        elif(ch==3):
            m=input("Enter Customer's  mobile no be searched : ")
            cur=self.__con.cursor() #to connect the table into connection string
            query="SELECT * FROM customer where mobile=%s" 
            try:
                cur.execute(query,m)
            except Exception:
                print("Query Error")
            else:
                result=cur.fetchall()
                print(result)
                cur.close()
        elif(ch==4):
            c=input("Enter Customer's City to be searched : ")
            cur=self.__con.cursor() #to connect the table into connection string
            query="SELECT * FROM customer where city=%s" 
            try:
                cur.execute(query,c)
            except Exception:
                print("Query Error")
            else:
                result=cur.fetchall()
                print(result)
                cur.close()
        else:
            print("Invalid choice ")

    def update_record(self):
        pass

    def delete_record(self):
        cur=self.__con.cursor()
        query="DELETE FROM customer where custid=%s"
        cid=int(input("Enter Customer Id to be Deleted: "))
        try:
            cur.execute(query,cid) #Query run
        except Exception:
            print("Query Error")
        else:
            print("Record Delete successfully in table")
            self.__con.commit()
            cur.close()
    def menu(self):
        print("1. Insert Record ")
        print("2. View All Records ")
        print("3. View Particular Record : ")
        print("4. Update Record : ")
        print("5. Delete Record : ")
        print("6. Exit the Program ")
#Main program
#call login page
u1,p1=login.login_page() #call function
if(u1!=None and p1!=None):
    #create the object of Bank class
    B=Bank()
    while(True):
        B.menu()
        choice=int(input("Enter Yout Choice : "))
        if(choice==1):
            B.insertrecord()
        elif(choice==2):
            B.selectallrecord()
        elif(choice==3):
            B.select_particular_record()
        elif(choice==4):
            B.update_record()
        elif(choice==5):
            B.delete_record()
        elif(choice==6):
            break #Exit from loop
        else:
            print("Invalid choice")
else:
    print("Userid and password does not match ")
    
del(B) #call destructor

        






        
