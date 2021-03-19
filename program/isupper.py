while(True):
    name=input("Enter name in capital letter : ")
    if(name.islower()): #if input in capital letter then process
        print("Name : ",name)
        break
    else:
        print("Please enter name in capital letter")
