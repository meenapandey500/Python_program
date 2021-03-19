from flask import Flask
app=Flask(__name__)

@app.route("/") #function decorator , its automatic call in browser
def hello(): #hello user defined function
    return "Welcome to India "

@app.route("/home")#function decorator
def msg():
    return "Hello, How are you"

#main program
app.run()
