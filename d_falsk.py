from flask import Flask, render_template, request
import pymysql
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
        en = details['fname']
        n = details['lname']
        a=23
        c='bpl'
        cur = con.cursor()
        query="INSERT INTO STUDENT(enroll,name,age,city)values(%s,%s,%s,%s)"  #%s means string
        val=(en,n,a,c) #val tuple variable
        cur.execute(query,val)
        con.commit()
        #cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
