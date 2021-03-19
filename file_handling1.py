#to store data in file and read it
def writefile():
    t=open("content.txt","w") #write mode
    t.write("\n Python is a general purpose, high level and object oriented language")
    t.write("\n Python is a dynamic datatype ")
    t.write("\n Pytohn is a open data source ")
    t.close()
def readfile():
    #To open file in read mode
    try:
        t=open("content.txt","r")
    except FileNotFoundError:
        print("File not found ")
    else:
        print(t.read()) #to read all data from file
        t.close()
#main program
while(True):
    print("\n 1. write \n 2. read \n 3. Exit ")
    ch=int(input("Enter Your choice : "))
    if(ch==1):
        writefile()
    elif(ch==2):
        readfile()
    elif(ch==3):
        break #exit from loop
    else:
        print("Invalid choice")
