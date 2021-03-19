a=10 #global variable

def show():
    global a
    print("value of a : ",a)
    a=a+3
    print("After increment , value of a : ",a)
def show1():
    global a
    print("value of a : ",a)
    a=a*2
    print(a)
#main program
#call function
show()
show1() #call
print("a=",a)
