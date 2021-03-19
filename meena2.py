from flask import Flask,render_template

app=Flask(__name__)

#create function decorator
@app.route("/")
def index():
    return "Welcome"

@app.route("/home")
def home():
    name="Meena"
    t="HTML Page"
    return render_template('meena2.html',title=t,username=name)

#main program
app.run(debug=True)

#save path of python :- meena2.py
