'''
x=input("Enter NUmber x : ")
y=input("Enter number y : ")
z=input("Enter number z : ")'''
while(True):
    x,y,z=input("Enter number x,y and z : separator between 2 variables from space").split(",")
    # separator between 2 input : comma  but x,y and z hold string value
    if(x.isdigit() and y.isdigit() and z.isdigit()):
        sum=int(x)+int(y)+int(z)
        print("sum : ",sum)
        break #exit from loop
    else:
        print("please enter integer value")
