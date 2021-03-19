from flask import Flask,render_template

app=Flask(__name__)

#create function decorator
@app.route("/")
def index():
    return "Welcome"

@app.route("/home")
def home():
    users=["Meena","Rekha","Anu","Tina"] #create the list of users
    t="User Name"
    return render_template('meena3.html',title=t,username=users)

#main program
app.run(debug=True)

#save meena3.py
