#Wap to find the sum of 2 nos.
while(True):
    a=input("Enter NUmber a : ")  #accept string type
    if(a.isnumeric()) :  #outer if condition true
        b=input("Enter number b : ")
        if(b.isnumeric()):  #condition true   inner if 
            c=int(a)+int(b)
            print("sum : ",c)
            break #exit from loop
        else:   #inner else
            print("Invalid value of b ,Please enter integer value :")
        
    else :  #outer else
        print("Invalid value of a ,Please enter integer value :")
