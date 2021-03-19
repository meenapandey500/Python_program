try:
    a=int(input("Enter Number a : ")) 
    b=int(input("Enter Number b : "))
    c=int(input("Enter Number c : "))
    d=a/(b-c)    
    
    print("Answer  : ",d)   
except ValueError:
    print("Datatype Mismatch please enter integer value")
except ZeroDivisionError:
    print("Divide by Zero Error")

try:
    d=a+b+c
    print("sum : ",d)
except NameError:
    print("Variable not found")

print("Good Bye")
