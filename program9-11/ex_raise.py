#Raise an exception
try:
    age=int(input("enter Age : "))
    if(age<18):
        raise Exception("Age must be greater than >18")
except Exception as e:
    print(e)
else:
    print("Age : ",age)
