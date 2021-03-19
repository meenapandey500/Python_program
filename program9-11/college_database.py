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
#insert record
en=int(input("Enter Enrollment no. : "))
n=input("Enter Student Name ")  #varchar type in table=string
a=int(input("Enter Age : "))
c=input("Enter City :")
#to insert data from front end (python's output screen) to backend(sqlserver)
#the fire SQL Query
query="INSERT INTO STUDENT(enroll,name,age,city)values(%s,%s,%s,%s)"  #%s means string
val=(en,n,a,c) #val tuple variable
#prepared cursor
cur=con.cursor()
#run insert query
try:
    cur.execute(query,val)
except:
    print("Query Error")
else:
    #save in database  use commit()
    con.commit()
    print("Record Insert Successfully")
#close connection
con.close()
