#WAP to find the sum of 2 nos. 
while(True):
    try:
        a=float(input("Enter Number a : "))
        break #exit from loop
    except ValueError:
       print("Data Type Mismatch Error, Please Re-Enter numeric value of variable a : ")
print("Value of a : ",a)

while(True):
    try:
        b=int(input("Enter Number b : "))
        break #exit from loop
    except ValueError:
       print("Data Type Mismatch Error, Please Re-Enter Integer value of variable b : ")
print("Value of b : ",b)

c=a+b
print("Sum=",c)
