from flask import Flask,render_template
#render_template inbuilt class 

app=Flask(__name__)

@app.route('/admin/<user>') #function decorator <user> variable pass value of user on run time
def hello(user): #hello user defined function
    return render_template("m3.html",name=user)  #render_template() inbuilt function to call .html page
                                        #which save templates folder



#main program
app.run()
