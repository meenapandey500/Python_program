from flask import Flask  #flask inbuilt package and Flask inbuilt class
#step 1
app=Flask(__name__)  #__name__  inbuilt attributes of class
#app user defined object name

#create decorator function  means to run automatic in browser means decorator function
#automatic call
#@
@app.route("/") #function decorator , its automatic call in browser
def hello(): #hello user defined function
    return "Welcome to India "

#main program

app.run()  #run() inbuilt function

