from flask import Flask,render_template
#render_template inbuilt class 

app=Flask(__name__)

@app.route("/result")
def result():
    #create dictionary
    d={'physics':50,'chemistry':67,'maths':89}
    return render_template('m6.html',marks=d)


#main program
app.run()
