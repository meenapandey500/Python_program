#To view all records from table on output screen
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

#Fire Select Query
query="SELECT * FROM STUDENT"
#prepared cursor
cur=con.cursor()
#run select query
cur.execute(query)
result=cur.fetchall()  #fetchone() to display only first record
print(result)
con.close()



