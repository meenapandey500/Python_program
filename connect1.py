
import pymysql #call library
# Step 1 :  #Create a connection string between python and mysqlserver
servername="localhost"
username="root"
password=""
dbname="SBI_Bank" #database name

#create object con : it is user defined object(collection of variables)
#Handle exception
try:
    con=pymysql.connect(servername,username,password,dbname)
    # con user defined object (object means collection of data)
except Exception:
    print("Connection Error")
else:
    print("Connection successfully created")
    

#step 2 :  Write a Query : To send data from o/p screen of python to table of database
    #of mysql server then use DML query of SQL : - insert record
#Query hold in string variable , SQL is not a case sensitive
query="INSERT INTO customer(custid,custname,address,mobile,city)VALUES(%s,%s,%s,%s,%s)"
#in Python , assign of query is a string variable

#step 3 RUN of any Query  : execute( ) inbuilt method of cursor()
#cursor() inbuilt of connect()
#run query : table==>database==>mysql server ==>user=root ==>password="" ,server=localhost
#path of database==>mysql server ==>user=root ==>password="" ,server=localhost is con object
#For run any query , First create a cursor
#create the cursor object using the inbuilt method cursor() which define
#pymysql.connect() class
cur=con.cursor() #create the cursor object : cur (connect table from connectionstring con)

#Step 3: Query run with the help of execute() method which define in cursor() class
#First input from user
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
#save record permanently into table then use Sql's command commit()
#commit() inbuilt method of connect()
con.commit()
cur.close() # close() the cursor means close() inbuilt method of cursor
con.close() #close() inbuilt method of connect() , its close a connection









    
