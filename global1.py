#global variable
a=5
def add( ):
    a=3  #local variable first preference local 
    c=a+8
    print("sum :",c)

#call in main program
add()  #call function
print("a=",a)
a=a+2 #editing value of global variable in main
print("a=",a)

