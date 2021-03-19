#Write a program to store data in file
t=open("msg.txt","a") #to open file in aapend mode
#here t temp file object
t.write("\n Python is a high level lang.")
t.write("\nIt is also Interpreted Lang.")
t.close() #close() inbuilt function to close temporary file
