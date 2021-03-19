#Input user's full name and mobile number and then store this information by writing
#it to  a text file in append mode. 

#Display all the users with their mobile numbers at the end of the program.

class information:
    def __init__(self): #constructor function
        self.name=input("Enter Full name : ")
        self.mobile=input("Enter MObile No. ")

    def writefile(self):
        f=open("student.txt","a") #to open file in append mode
        f.write(self.name+"\n"+self.mobile+"\n")
        f.close() #close the file
    def display(self):
        print("Information of Students : ")
        try:
            f=open("student.txt","r")
        except FileNotFound:
            print("File does not exist")
        for x in f:
            print(x)
        f.close()
#main program
info=information()  #create object of class information
info.writefile()
info.display()
