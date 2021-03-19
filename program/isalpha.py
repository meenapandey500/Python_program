while(True):
    password=input("Enter password : ")
    if(password.isalpha()):  #if condition is true
        print("Valid")
        
        break #exit from loop
    else:
        print("Not a valid ,please reenter the password (please enter only alphabet  ")
