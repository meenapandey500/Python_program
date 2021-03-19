class files:
    def writefile(self):
        with open("content.txt","w") as t : #or t=open("file.txt","w")  then compulsory t.close()
            t.write("Welcome to Itvedent\n Hello, How are You")
    def readfile(self):
        try:
            with open("content.txt","r") as t: #or t=open("file.txt","r")
                c=t.read()
        except FileNotFoundError as e:
            print(e)
        else:
            print(c)
    def copyfile(self):
        with open("content.txt","r") as t: #open inbuilt file content.txt in read mode
            c=t.read()
        with open("new_file.txt","w") as t1 :
            t1.write(c)
        with open("new_file.txt","r") as t1:
            c1=t1.read()
        print("New file data : ",c1)

