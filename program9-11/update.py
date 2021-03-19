#To update city of  particular record from table according to enroll
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
en=int(input("Enter enrollment no. to be updated : "))
c=input("Enter new city : ")
#Fire delete Query
query="UPDATE STUDENT SET CITY=%s WHERE enroll=%s"
#prepared cursor
cur=con.cursor() #to keep cursor on particular path
val=(c,en)
#run update query
try:
    cur.execute(query,val)
    con.commit() #to changes permanently in table
    print(" Record Update  successfully")
except:
    print("Record not found")
con.close()



