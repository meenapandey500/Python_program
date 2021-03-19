#WAP to check the given number is Armstrong number or not .
n=int(input("Enter NUmber : ")) #suppose n=153
s=n
r=str(n)
x=len(r)
print("No. of digit : ",x) 
sum=0
while(n>0):  
    y=n%10
    sum=sum+(y**x)
    n=n//10
print("sum : ",sum)  
if(sum==s):  
    print("This number is Armstrong number")
else:
    print("Number is not a armstrong number")
    
