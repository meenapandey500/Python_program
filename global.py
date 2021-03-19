pi=3.14 #global variable

def aoc(r):
    return(pi*r*r)

def volume_sphere(r):
    return(4/3*pi*r**3)

#call in main
print("value of pi : ",pi)
r=int(input("Enter radius : "))
a=aoc(r) #call function
print("area of cirlce : ",a)
a=volume_sphere(r)
print("Volume of sphere : ",a)
