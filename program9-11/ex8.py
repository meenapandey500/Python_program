while(True):
    try:
        a=int(input("Enter NUmber a : "))
        break
    except ValueError:
        print("Invalid input,please reenter value of a")

while(True):
    try:
        b=int(input("Enter NUmber b : "))
        break
    except ValueError:
        print("Invalid input,please reenter value of b")
c=a+b
print("sum : ",c)
    
