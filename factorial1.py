#WAP to find the factorial of given number using Iteration(loop)
def fact(n): #fact() user defined function , passing arguments and return value
    ans=1
    while(n>0):
        ans=ans*n
        if(n!=1):
            print(n,"*",end="")
        else:
            print(n,end="")
        n=n-1
    return ans
   
#main program
n=int(input("Enter Number : "))
ans=fact(n) #call function
print("=",ans)
