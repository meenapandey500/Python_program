#to update the record of student table
# to change the city with delhi whose enroll=102
import pymysql
#stepn 1 : to create a connection string
#create the object of connect() : con
servername="localhost"
username="root"
password=""
dbname="school_mgmt"  #database name
try:
    con=pymysql.connect(servername,username,password,dbname)
except Exception:
    print("Connection Error")
else:
    print("Connection successfully ")
#step 2 : create a cursor
#create the object of cursor cur cursor() inbuilt method of connect class)
cur=con.cursor()

#step 3 : Query fire on table
c=input("Enter new city : ")
en=int(input("Enter Enrollment No. : "))
query="UPDATE student set city=%s where enroll=%s" #%s string unknown
#where use for condition

#Query run , use execute method , this is inbuilt method of cursor
val=(c,en)
try:
    cur.execute(query,val)
except Exception:
    print("Query Error")
else:
    print("Record Update successfuuly")
#step 4:
    con.commit() #to changes parmenently in table
cur.close() #close() inbuilt method of cursor
con.close()#close() inbuilt method of connect

