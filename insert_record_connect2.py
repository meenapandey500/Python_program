
import pymysql #call library
# Step 1 :  #Create a connection string between python and mysqlserver
servername="localhost"
username="root"
password=""
dbname="SBI_Bank" #database name

try:
    con=pymysql.connect(servername,username,password,dbname)
    # con user defined object (object means collection of data)
except Exception:
    print("Connection Error")
else:
    print("Connection successfully created")

#step 2 :
    cur=con.cursor()
#step 3:
while(True):  
    
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

    con.commit()
    ans=input("Add another Records of customer y/n")
    if(ans=="n" or ans=="N"):
        break #exit from loop

    
cur.close() # close() the cursor means close() inbuilt method of cursor
con.close() #close() inbuilt method of connect() , its close a connection









    
