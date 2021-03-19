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

#input enroll from user which is deleted
en=int(input("Enter Enrollment no. to be deleted : "))

#step 3 : Query fire  of delete according to enroll
query="DELETE FROM student where enroll=%s"

#step 4: Query run with the help of cursor
try:
    cur.execute(query,en)
except Exception:
    print("Query Error")
else:
    print("Delete Record successfully")
    con.commit() #save changes permanently in table
cur.close()
con.close()



