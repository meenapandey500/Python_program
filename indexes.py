from flask import Flask, render_template, request
#from flask_mysqldb import MySQL
import pymysql
app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        return firstName+" "+lastName
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
