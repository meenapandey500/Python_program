try:
    a=int(input("Enter number a  : "))
    b=int(input("Enter number b : "))
    c=int(input("Enter number c : "))
    d=a/(b-c)
except ValueError:
    print("Invalid Input, please enter integer type value ")
except Exception:
    print("Divide by zero error")
else:
    print("Result : ",d)
