#To open file in read mode and read all lines and hold on list format then  use readlines()
try:
    t=open("content.txt","r")
except FileNotFoundError:
    print("File not found ")
else:
    X=t.readlines() #to read all lines from files and show in list format
    #here X is a list object
    print(X)
    print("Show 2 nd line of file : ",X[1])
    t.close()
