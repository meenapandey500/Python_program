#CUSTOM ERROR
#mobile no. only 10 digits

name=input("Enter Name : ")
try:
    mobile=int(input("Enter Mobile No. : "))
    #find the length of mobile
    mobile=str(mobile) #mobile change string type
    x=len(mobile) #len() to find the no. of characters in given string
    if(x<10):
        raise ValueError  
    elif(x>10):
        raise Exception
except ValueError:
    print("Mobile no. not less than 10 ")
except Exception:
    print("Mobile no. not greatesr than 10")
else:
    print("Name : ",name)
    print("Mobile No. : ",mobile)
