#local variable and global variable
a=10 #global variable

def show():  #no passing argument
    a=5  # here a is a local variable
    print("value of a = ",a)
def show1():
    print(a)
#call
show()
show1()
print("value of a : ",a)
