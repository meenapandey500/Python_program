from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)


#create function decorator
@app.route('/success/<name>')
def success(name):
    return "Welcome %s" % name

@app.route('/')
def hello():
    return render_template('meena4.html')


@app.route("/meena4",methods=['POST','GET'])
def login():
    if request.methods=='POST':
        user=request.form['uname']
        return redirect(url_for('success',name=user))
    else:
        return render_template('meena4.html')
    
#main program
app.run(debug=True)

#save meena4.py
