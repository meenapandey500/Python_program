a=int(input("Enter NUmber a : "))
b=int(input("Enter NUmber b : "))
try:
    c=a/b
    print("divide : ",c)
except Exception as e:
    print("Divide by zero error")
    print(e)

c=a+b
print("sum : ",c)
