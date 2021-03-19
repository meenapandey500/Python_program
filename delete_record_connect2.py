#WAP To delete record from table according to Customer ID 
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
    
    query="DELETE FROM customer where custid=%s"

    cid=int(input("Enter Customer Id to be Deleted: "))
    
    try:
        cur.execute(query,cid) #Query run
    except Exception:
        print("Query Error")
    else:
        print("Record Delete successfully in table")

    con.commit()
    ans=input("Delete  another Records of customer y/n")
    if(ans=="n" or ans=="N"):
        break #exit from loop

    
cur.close() # close() the cursor means close() inbuilt method of cursor
con.close() #close() inbuilt method of connect() , its close a connection









    
