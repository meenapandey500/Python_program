#WAP to find the factorial of given number using Recursion
def fact(n): #fact() user defined function , passing arguments and return value
    if(n==0):
        return 1
    else:
        return(n*fact(n-1))

#main program
n=int(input("Enter Number : "))
ans=fact(n) #call function
print("Factorial : ",ans)
