def division(a,b): #USer defined function, passing argument but no return value
    try:
        c=((a+b)/(a-b))
    except Exception as e: #Exception inbuilt error class this is general error class
        print(e)
        print("divide by zero error")
    else:
        print("Answer : ",c)

#main program
a=int(input("Enter Number a  : "))
b=int(input("Enter number b : "))
division(a,b) #call function
