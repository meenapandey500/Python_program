from flask import Flask  #here flask  inbuilt package of python and Flask inbuilt class
#Flask inbuilt class which define in package flask

app=Flask(__name__) #app user defined object its work as constructor function
#means automatic call file name which is run

#declare function decorator means this function is automatic call in browser when run the
#program which write in file .py
@app.route("/")
def hello():  #hello() user defined function
    return "Hello How are you "


#main program
app.run() #run inbuilt function

