#Write a program to find all three digit Armstrong nos and also print the count.
c=0
for x in range(100,1000):
    n=x
    sum=0
    while(n>0):
        y=n%10
        sum=sum+y**3
        n=n//10
    if(x==sum):
        c=c+1
        print("{} is armstrong no.".format(x))

print("No. of Armstromg no. of all three digits : ",c)    
