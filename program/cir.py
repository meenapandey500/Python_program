#default parameter
def area(r,pi=3.14):
    return pi*r*r
#main program
r=int(input("Enter radius : "))
#call function
ar=area(r)
print("area of circle : ",ar)
