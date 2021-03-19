#Login Page
import pymysql #call library
def login_page():
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

    #step 2 : Create a cursor
    cur=con.cursor()
    #step 3 :
    #Query fire : select
    query="SELECT * FROM login where userid=%s and password=%s" #and logical operator

    u=input("Enter Userid : ")
    p=input("Enter Password :")
    #create a tuple
    val=(u,p)
    #step 4: Select Query Run :
    try:
        cur.execute(query,val)
    except Exception:
        print("Query Error")
    else:
        result=cur.fetchall()
        try:
            u1=result[0][0]
            p1=result[0][1]
            cur.close()
            con.close()
            
        except Exception:
            print("Userid and password doesnot match")
        else:
            return u1,p1






