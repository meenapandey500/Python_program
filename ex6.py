#wap to store name and mobile no. of employee but mobile does not less than or greater than
#10 , exact 10 digit
name=input("Enter Name of Employee : ")
while(True):
    mobile=int(input("Enter Mobile No. : "))
    mobile=str(mobile) #to converts int value to string value
    x=len(mobile) #len() to find the no. of digits /chars in given string
    try:
        if(x!=10):
            raise Exception("Mobile No. should be  10 digit please re-enter Mobile no. ")
    except Exception as e:
        print(e)
    else:
        print("Employee Name : ",name)
        print("Mobile No. : ",mobile)
        break #exit from loop
