#WAP to read data from file and store in list use readlines( ) inbuilt function
t=open("msg.txt","r") #to open file in read mode
list1=t.readlines()
print(list1)
print(list1[1]) #access data from list at 1st index
t.close()
