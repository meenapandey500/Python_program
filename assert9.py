#wap to store name and mobile no. of employee but mobile does not less than or greater than
#10 , exact 10 digit  use asserion
name=input("Enter Name of Employee : ")
while(True):
    mobile=int(input("Enter Mobile No. : "))
    mobile=str(mobile) #to converts int value to string value
    x=len(mobile) #len() to find the no. of digits /chars in given string
    try:
        assert (x==10), "Mobile No. should be  10 digit please re-enter Mobile no. " #error msg
        print("Employee Name : ",name)
        print("Mobile No. : ",mobile)
        break #exit from loop
    except AssertionError as msg:
        print(msg)
    
#syntax of assert
#assert(condition) , "error"
#process
       
