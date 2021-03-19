f=open("student.txt","a") #to open file in append mode
while(True):
    name=input("Enter Full name : ")
    mobile=input("Enter MObile No. ")
    f.write(name+"\n"+mobile+"\n")
    ans=input("Add another records of student y/n :")
    if(ans=="n" or ans=="N"):
        break #exit from loop
    
f.close() #close the file
#To read data from file
print("Information of Students : ")
try:
    f=open("student.txt","r")
except FileNotFound:
    print("File does not exist")
for x in f:
    print(x)
f.close()

