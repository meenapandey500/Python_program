#WAP to check the given number is prime number or not
n=int(input("Enter Numer  : ")) #suppose n=7     n=5

if(n>1):
    for i in range(2,n) : #i=2(start=2) i<n(stop=n-1) i=i+1(step=+1) i=2 stop=6
        if (n%i==0): #if(7%2==0) false 7%3==0 F  7%4==0 F 7%5==0 F 7%6==0 F
            print(n, " is not a prime number ")
            break #exit from for loop
    else:  #else of for loop
         print(n," is a prime number")  #7 is a prime no.
else:  #else of if
    print(n, " is not a prime number ")
