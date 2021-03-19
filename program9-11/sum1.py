a=input("Enter NUmber a : ")
b=input("Enter NUmber b : ")
try:
    c=int(a)+int(b)
    print("sum = ",c)
except Exception as e: #here Exception inbuilt class and e object name of class Exception
    print(e)
    print("Invalid input")
    
print("Welcome ")
