'''t=open("hello.txt","w")
t.write("Meena, How are you\n")
t.write("I am fine and you")
t.close()'''
#write data in file
with open("hello1.txt","w") as t :  #with open("permanentfile.txt","mode") as temporary file
      t.write("Meena, How are you\n") ##here t temp file  
      t.write("I am fine and you")                                
#never close the temporary file if use with

#read data from file
with open("hello1.txt","r") as t :
    for x in t.readlines():
        print(x)
