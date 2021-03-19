#Write a program to find the square of given number 
def square(a=1):  #default argument
    return a*a
#main program
a=int(input("Enter Number a  : "))
#call function
ans=square(a)
print("Square : ",ans)
ans=square() #call function but no pass any parameter
print("Square : ",ans)
