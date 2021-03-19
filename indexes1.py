from flask import Flask, render_template, request
#from flask_mysqldb import MySQL
import pymysql
app = Flask(__name__)

'''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'
'''

#mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
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

#step 2 :
        cur=con.cursor()
        query="INSERT INTO customer(custid,custname,address,mobile,city)VALUES(%s,%s,%s,%s,%s)"
        #create tuple (immutable)
        val=(207,firstname,lastname,firstname,lastname)
        try:
            cur.execute(query,val) #Query run
        except Exception:
            return ("Query Error")
        else:
            return ("Record Insert successfully in table")

        con.commit()                  
        return "success"
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
