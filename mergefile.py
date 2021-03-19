#to merge a file

with open("file1.txt","w") as t:   
    t.write("Hello, how are you")

    
with open("file2.txt","w") as t:   
    t.write("I am Fine and you")


#to open file in read mode file1
with open("file1.txt","r") as t:   
    content1=t.read()


#to open file in read mode file2
with open("file2.txt","r") as t:   
    content2=t.read()

#merge file : and stored in new file3.txt
#to open file in read mode file1
with open("file3.txt","w") as t:   
    content=content1+"\n"+content2
    t.write(content)

#to open file3(merge file in read mode 
with open("file3.txt","r") as t:   
    print(t.read())



    

