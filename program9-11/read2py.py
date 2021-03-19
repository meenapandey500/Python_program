#WAP to read data from file
t=open("msg.txt","r") #to open file in read mode

content=t.read(5)  #here 5 means only read 5 chars from starting
print(content) #to print data in output screen
content=t.read(5)
print(content)
t.close()
