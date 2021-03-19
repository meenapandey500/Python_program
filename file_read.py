#To read data from file
t=open("msg.txt","r") #to open file in read mode
content=t.read(5) #5 means only read 5 chars from start
print(content)
content=t.read(5) #to show read from start 6th char and displat total 5 chars
print(content)
