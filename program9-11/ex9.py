try:
    a=int(input("Enter NUmber a : "))
    b=int(input("Enter NUmber b : "))
    c=a/b
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("NUmber is not divided by zero")
else:
    print("divide=",c)
finally: #always execute
    print("Good Bye")
    
