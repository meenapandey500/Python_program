from flask import Flask
app=Flask(__name__)

#Function decorator
@app.route('/')
def home():
    return "Hello,How are you"

#Function decorator
@app.route('/admin')
def show():
    return "Meena Pandey"

#main program
app.run()  #run a program
