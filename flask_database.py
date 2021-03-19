from flask import Flask, render_template, request
#from flask_mysqldb import MySQL
import pymysql
app = Flask(__name__)

servername="localhost"
username="root"
password=""
dbname="SBI_Bank"
try:
    con=pymysql.connect(servername,username,password,dbname)
except Exception:
    msg= "Connection Error"
else:
    msg="Connection successfully created"

@app.route('/')
def connect():
    return msg

@app.route('/insert', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        query="insert into login values(%s,%s)"
        cur=con.cursor()
        val=(firstName,lastName)
        cur.execute(query,val)
        con.commit()
        
        return "Record Insert successfully in table"
    return render_template('index.html')

@app.route('/select')
def select():
    query="select * from login"
    cur=con.cursor()
    cur.execute(query)
    result=cur.fetchall()
    return render_template('select.html',data=result)

if __name__ == '__main__':
    app.run(debug=True)
