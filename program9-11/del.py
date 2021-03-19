#To delete particular record from table according to enroll
#Call library pymysql
import pymysql
#to create a connection string (between python and mysqlserver)
servername="localhost"
username="root"
password=""
dbname="college1"
try:
    con=pymysql.connect(servername,username,password,dbname)
except:
    print("Connectivity Error")
else:
    print("Connect successfully")
en=int(input("Enter enrollment no. to be deleted : "))
#Fire delete Query
query="delete FROM STUDENT WHERE enroll=%s"
#prepared cursor
cur=con.cursor()
#run delete query
try:
    cur.execute(query,en)
    con.commit() #to changes permanently in table
    print("Delete Record successfully")
except:
    print("Record not found")
con.close()



