from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home')  
def hello():  
    return "hello, welcome to our website";  
  
if __name__ =="__main__":  
    app.run(debug = True)  
