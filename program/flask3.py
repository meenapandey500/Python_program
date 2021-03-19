from flask import Flask,render_template
#render_template inbuilt class 

app=Flask(__name__)

@app.route("/admin") #function decorator 
def hello(): #hello user defined function
    return render_template("m2.html")  #render_template() inbuilt function to call .html page
                                        #which save templates folder



#main program
app.run()
