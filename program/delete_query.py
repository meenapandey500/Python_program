#to delete the record from student table
# to delete a particular record of student according to enrollment no.
import pymysql
#step 1 : to create a connection string
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
en=int(input("Enter Enrollment No. to be deleted: "))
query="DELETE from student where enroll=%s" #%s string unknown
#where use for condition

#Query run , use execute method , this is inbuilt method of cursor
try:
    cur.execute(query,en)
except Exception:
    print("Query Error")
else:
    print("Record Delete successfully")
#step 4:
    con.commit() #to changes parmenently in table
cur.close() #close() inbuilt method of cursor
con.close()#close() inbuilt method of connect

