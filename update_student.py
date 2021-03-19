import pymysql
from flask import *  
app = Flask(__name__)

servername="localhost"
username="root"
password=""
dbname="college1"
con=pymysql.connect(servername,username,password,dbname)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        en = details['enroll']
        c= details['city']
        
        cur = con.cursor()
        query="UPDATE STUDENT SET CITY=%s where enroll=%s"  #%s means string
        val=(c,en) #val tuple variable
        cur.execute(query,val)
        con.commit()
        return 'successfully update record'
    return render_template('update.html')
#main program
app.run()  
