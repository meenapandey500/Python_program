#multiple value input from one input() function using list comprehension
a,b,c=[int(x) for x in input("Enter 3 Numbers separate by space : ").split() ]
print("a=",type(a))
print("b=",b)
print("c=",c)

#List compression
#[expression for var in ...]
