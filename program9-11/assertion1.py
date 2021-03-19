#Assertion
try:
    age=int(input("enter Age : "))
    assert age>18,"Age must be entered >18."
    print("Age : ",age)
except AssertionError as msg:   #AssertionError inbuilt error class 
    print(msg)                  #msg user defined object of AssertionError class
