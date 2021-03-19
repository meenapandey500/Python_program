#Main program
from Manipulation import Data_Manipulation

#create the object of class

d1=Data_Manipulation()
while(True):
    d1.menu()
    ch=int(input("Enter Your choice : "))
    if(ch==1):
        d1.insert_record()
    elif(ch==2):
        d1.View_Record()
    elif(ch==3):
        d1.Search_Record()
    elif(ch==4):
        d1.update_Salary()
    elif(ch==6):
        d1.delete_record()
    elif(ch==7):
        break
    
