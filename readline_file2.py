#To open file in read mode and data read line by line  use readline()
try:
    t=open("content.txt","r")
except FileNotFoundError:
    print("File not found ")
else:
    for line in t:
        print(line)
    t.close()
