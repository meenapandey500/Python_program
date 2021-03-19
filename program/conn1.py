#insert record into table
import pymysql
import connect as cn  #connect filename

con1=cn.connection() #call function

#create cursor
cur=con1.cursor() 

en=int(input("Enter enrollment no. : "))
n=input("Enter Name of student : ")
a=int(input("Enter Age : "))
c=input("Enter City : ")
q="insert into student values(%s,%s,%s,%s)"
#create tuple
val=(en,n,a,c)
#query run
try:
    cur.execute(q,val)
except Exception:
    print("Query error")
else:
    con1.commit() #to save record permanently into table
    print("Record insert successfully")
    con1.close()
    


