while(True):
    password=input("Enter password : ")
    if(password.isalnum()):  #if condition is true
        print("Valid")
        break #exit from loop
    else:
        print("Not a valid ,please reenter the password (please enter alphabet and number: ")
