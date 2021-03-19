#extension .txt , csv ,dbf, docx ,xlsx
def readfile(): #user defiend function
    filename=input("Enter filename to be read : ")
    extension=input("Enter extension of file : ")
    file=filename+"."+extension
    print("filename=",file)
    try:
        t=open(file,"r+") #to open file in read mode
    except FileNotFoundError:
        print(file," not found ")
    else:
        for i in t.readlines():
            print(i)
        t.close()
        
    finally:  #this always run
       print("Good Bye")
    
def writefile():
    filename=input("Enter filename to be write : ")
    extension=input("Enter extension of file : ")
    file=filename+"."+extension
    print("file=",file)
    t=open(file,"a+") #to open file in append mode
    name=input("Enter name of student : ")
    mobile=int(input("Enter Mobile No. : "))
    s=name+","+str(mobile)+"\n"
    t.write(s)
    t.close()
def menu():
    print("\n1. Write \n2. Read \n3. Exit ")
#main program
while(True):
    menu() #call menu
    ch=int(input("Enter your choice : "))
    if(ch==1):
        writefile() #call
    elif(ch==2):
        readfile() #call
    elif(ch==3):
        break
    else:
        print("invalid choice : ")
