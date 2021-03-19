'''
    write a program for book management system using file handling
    data must be stored in comma separated value (we create a csv)by default create txt file
    csv means tabular form means no. of records , in each record many columns
'''
class Book: #Book user defined class name

    def writeData(self):  #user defined function(member function)
        bid=input("Enter Book ID => ")
        name=input("Enter Book Name => ")
        price=float(input("Enter Book price =>"))

        s=bid+','+name+','+str(price)+'\n' #here s means string object 

        f=open("Book.csv","a+")  #here f temporary file and Book.csv it is permanent file
        #a means append mode
        f.write(s) #write( )  inbuilt method to write data in temporary file f
        f.close()

    def readData(self):  #user defined function (member function)
        f=open("Book.csv","r+") #to open file in read and f temporary file
        for i in f.readlines():  #readline()  read( )
            print(i)
        f.close()

#Main program
b=Book()  #create the object of class
while True:
    b.writeData()
    ch=input("Add more book or do you want to continue ...! (y/n) => ")
    if ch in('y','Y'):   #if(ch=='Y' or ch=='y'):
        continue
    else:
        break #exit from loop
b.readData()
