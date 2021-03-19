def simple_interest(p,r,t): 
    return(p*r*t/100)

#main program
pr=float(input("Enter principal:"))
rate=float(input("Enter rate :"))
time=int(input("Enter time :"))
#call function
d=simple_interest(pr,rate,time) #positional argument
print("simple_interest : =",d)

#but
d=simple_interest(r=rate,t=time,p=pr) #keyword argument
print("simple_interest : =",d)
