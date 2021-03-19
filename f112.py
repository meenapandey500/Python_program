from flask import Flask  

app=Flask(__name__) 

@app.route("/")
def hello():  #hello() user defined function
    return "Hello How are you "

@app.route("/Admin")
def msg():
    return "Hello Admin"

#main program
app.run() #run inbuilt function

