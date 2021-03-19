#Exception handling : to handle run time error
#WAP to find the sum of 2 nos.
while(True):
    try:
        a=int(input("Enter number a : "))
        break #exit from loop
    except Exception as e:  #Exception general inbuilt error class 
        print(e)

while(True):
    try:
        b=int(input("Enter number b : "))
        break #exit from loop
    except Exception:
        print("Invalid input of b,please Re-enter the Integer value of b : ")    
c=a+b 
print("sum : ",c)
try:
    c=a/b
except Exception as e:  #e alias name
    print(e)

print("Bye-Bye")
