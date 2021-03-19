#variable length argument
#WAP to find the sum of no. of elements using function
def addition(*var):
    s=0
    for i in var:
        s=s+i
    return s

#main program
a,b,c,d,e=[int(x) for x in input("Enter 5 Numbers separate by space : ").split() ]
s=addition(a,b,c,d,e)
print("Sum of 5 nos. : ",s)
