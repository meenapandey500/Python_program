#WAP to read data line by line from file
t=open("msg.txt","r") #to open file in read mode

content=t.readline()  #read first line
print(content) 
content=t.readline()  #read second line
print(content)
content=t.readline()   #read third line
print(content) 
t.close()
