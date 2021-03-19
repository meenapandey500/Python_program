#To display particular record from table according to enroll
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
en=int(input("Enter enrollment no. to be searched : "))
#Fire Select Query
query="SELECT * FROM STUDENT WHERE enroll=%s"
#prepared cursor
cur=con.cursor()
#run select query
try:
    cur.execute(query,en)
    result=cur.fetchall()  #fetchone() to display only first record
    print(result)
except:
    print("Record not found")
con.close()



