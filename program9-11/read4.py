#WAP to read data line by line from file use for loop
t=open("msg.txt","r") #to open file in read mode
for line in t:
    print(line) 

t.close()
