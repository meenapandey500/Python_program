#Example of local and global variable
b=7 #global variable Its call any function in this file
def addition() :
    a=4   #local variable , it will not call outside the function
    c=a+b
    print("sum=",c)
def subtract( ):
    a=8
    b=2
    c=a+b
    print("suntract=",c)
    
#main program
addition( ) #call function
print("b=",b)
subtract()

