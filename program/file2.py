'''with open("hello1.txt","r") as t :
    print(t.read(10)) #to read only first 10 characters
    #check current cursor position then use inbuilt function tell()
    print("Current position of cursor : ",t.tell())
    print(t.read(10))
    print("Current position of cursor : ",t.tell())
    #Reposition cursor pointer at the begining once again
    position=t.seek(0,0) #here 0 means 2nd char
    print(t.read(10))'''
