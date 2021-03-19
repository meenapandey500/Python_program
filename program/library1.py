def addition(x,y):   #here a and b variables are formal parameter /arguments or local variables
    z=x+y
    return z
def subtraction(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def menu():  #no passing arguments and no return value
    print("\n 1. sum \n 2. subtract \n 3. multiply \n 4. divide \n 5. exit ")
def swap(a,b):
    a,b=b,a
    return a,b
def fibonacci(a,b,n):  #passing arguments but no return value
    for i in range(1,n+1):
        c=a+b
        print(c)
        a=b
        b=c
    
    
