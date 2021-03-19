#no passing arguments/parameters but return value
def simple_interest():
    p,r,t=[float(x) for x in input("Enter Principal,Rate and Time separate by space : ").split()]
    return p*r*t/100

#main program
si=simple_interest() #call function
print("Simple Interest : ",si)
