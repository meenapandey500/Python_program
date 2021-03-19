a=5  #global variable
def increment( ):
    global a  #declare means edit the value of global variable
    print(a)  #5
    a=a+2  #a=7
    print(a)  #7
def show():
    print("a=",a) #7
    
    
#main program
show()  #5
increment()
show() #call 

