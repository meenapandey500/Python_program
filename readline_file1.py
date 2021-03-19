#To open file in read mode
try:
    t=open("content.txt","r")
except FileNotFoundError:
    print("File not found ")
else:
    print(t.readline())  #to show only first line means only one line
    print(t.readline()) #to show second line
    print(t.readline()) #to show third line
    print(t.readline()) #to show fourth line
    print(t.readline()) #to show fifth  line
    t.close()
