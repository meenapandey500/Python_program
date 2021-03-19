#To store data of students in file , ask the filename on run time from output screen
'''student's data :  enrollno,name,mobile no. on many students
student's data means database means table type means to store data in the form of
rows and columns means
Enroll,name,mobile  here enroll,name and mobile column name
110,"reeta",4567890987
120,"ritu",6789087666
csv file means comma separated values means create a csv file and store in bydefault path'''

def writefile():
    filename=input("Enter Filename : ") #string type
    extension=".csv" #string type
    filename=filename+extension #concatenate filename and extension and store in filename
    #to open this file in append mode
    print(filename)
    s=open(filename,"a") #here s temporary file name 
    enroll=int(input("Enter Enrollment no. : "))
    name=input("Enter Student Name : ")
    while(True):
        mobile=int(input("Enter Mobile No. : "))
        mobile=str(mobile)
        x=len(mobile)
        try:
            if(x!=10):
                raise Exception("Mobile no. should be 10 digit ")
        except Exception as e:
            print(e)
            print("Please re-enter 10 digits mobile no.")
        else:
            break #exit from loop
    
      #to store data in temporary file s
    data=str(enroll)+','+name+','+str(mobile)+'\n'  #concatenate
    s.write(data)
    s.close()

def readfile():
    filename=input("Enter Filename : ") #string type
    extension=".csv" #string type
    filename=filename+extension #concatenate filename and extension and store in filename
    print("File name : ",filename)
    #to open this file in read mode
    try:
        s=open(filename,"r") #here s temporary file name
    except FileNotFoundError:
        print("{} is not found".format(filename))
    else:    
        print("Student's Details ")
        for record in s: #by default read line by line 
            print(record)
        s.close()
    
#main program
while(True):
    print("\n1. Write Data \n2. Read data \n3. Exit")
    ch=int(input("Enter Your choice : "))
    if(ch==1):
        writefile()
    elif(ch==2):
        readfile()
    elif(ch==3):
        break
    else:
        print("Invalid choice")




