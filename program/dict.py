#create a dictionary
student={"rollno":110 ,"name" : "Anu Agrawal","Age":23,"City":"Mumbai"}
print("Type of student :",type(student))
#Loop through a Dictionary student
print("Keys are : ")
for x in student:  #only access key of dictionary stduent
    print(x)
print("Values are : ")
for x in student.values():  #only access value of dictionary stduent
    print(x)
