#WAP to read data from file
t=open("msg.txt","r") #to open file in read mode
#msg.txt : if msg.txt file exist then open this file in read mode otherwise error show
content=t.read( )  #content user defined object
print(content) #to print data in output screen
t.close()
