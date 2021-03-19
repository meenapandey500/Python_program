class bank:
    def __init__(self): #constructor function
        self.__cusid=int(input("Enter Customer Id : "))
        self.__ano=int(input("Enter Account no. : "))
        self.__cname=input("Enter Customer Name : ")
        self.__balance=0 
        print("Account Opened ....")

    def deposit(self):
        amt=float(input("Enter Deposit Amount" ))
        self.__balance=self.__balance+amt
        print(amt," deposit successfully: ")
    def withdrawl(self):
        amt=float(input("Enter withdrawl Amount" ))
        if(self.__balance>amt):
            self.__balance=self.__balance-amt
            print(amt," withdrawl successfully: ")
        else:
            print("Sorry, Insufficient Balance : ")
    def check_balance(self):
        print("Balance : ",self.__balance)
    def menu(self):
        print("\n 1.Balance check \n 2. deposit \n 3. withdrawl\n 4. Exit")
    def __del__(self): #destructor function
        print("Memory clear")
#main program
#create object of class bank
b=bank()
while(True):
    b.menu()
    ch=int(input("Enter Your choice : "))
    if(ch==1):
        b.check_balance()
    elif(ch==2):
        b.deposit()
    elif(ch==3):
        b.withdrawl()
    elif(ch==4):
        break 
    else:
        print("invalid choice")
#call destructor function : it is used to clear memory
del b  #del object name


