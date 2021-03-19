from flask import Flask,render_template
#render_template inbuilt class 

app=Flask(__name__)

@app.route('/admin/<int:marks>')  #bydefault variable string , if give int type then
def hello(marks):                 # use <int:variable>
    return render_template("m4.html",percent=marks)   #percent user defined variable



#main program
app.run()
