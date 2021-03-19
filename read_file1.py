#To open file in read mode
try:
    t=open("content.txt","r")
except FileNotFoundError:
    print("File not found ")
else:
    print(t.read(5)) #to read first 5 characters
    print(t.read(5)) #to read next 5 characters
    #initially the filepointer is at 0 use seek(cursor position) inbuilt function
    print(t.seek(0))  #cursor at first char 
    print(t.read(5))
    print("Current position of cursor : ",t.tell()) #tell() inbuilt function : to show
    print(t.seek(11))  #cursor at first char
    print("Current position of cursor : ",t.tell())
    print(t.read(10))
    #current position of cursor
    t.close()
