#Exception handling : to handle run time error
try:
    a=int(input("Enter number a : "))
    b=int(input("Enter number b : "))
except ValueError:  #ValueError inbuilt class
    print("Invaild Input ,please input integer value")
else:
    c=a+b
    print("sum=",c)

print("Bye-Bye")
