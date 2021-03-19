class filehandling:
    def __init__(self): #constructor function
        self.filenamename=input("Enter file name : ")
        self.filename=self.filename+".txt"
        
    def writefile(self):
        f=open("self.filename","w") #to open file in write mode
        f.write("Hello, How are you\n I am fine and You")

    def closefile(self):
        self.filename.close() #close file

    def readfile(self):
        print("Information of Students : ")
        try:
            f=open("self.filename","r")#to file in read mode
        except FileNotFound:
            print("File does not exist")
        for x in f:
            print(x)
        
#main program
info=filehandling()  #create object of class information
info.writefile()
info.closefile()
info.readfile()
info.closefile()

