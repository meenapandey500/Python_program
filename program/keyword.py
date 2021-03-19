#keyword arguments(passing argument but no  return value)
def show(name,age,city):
    print("Name : ",name)
    print("Age : ",age)
    print("City : ",city)
#main program
n=input("Enter name of student : ")
a=int(input("enter Age of student : "))
c=input("Enter City of student : ")
#call function
show(age=a,city=c,name=n)
