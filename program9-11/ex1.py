x=5
y=input("enter number y :")
try:
    print(x)
    print("sum=",x+int(y))
    f=open("msg.txt","r")
except NameError: #value of variable not found
    print("Variable x is not defined ")
except ValueError: #datatype mismatch
    print("value error")
except FileNotFoundError: #file not found 
    print("Something wrong,file does not exist")
except:
    print("Error")
