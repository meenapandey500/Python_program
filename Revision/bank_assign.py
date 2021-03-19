#Inheritance : single inheritance
class Customer:  #base class
    def __init__(self): #constructor function
        self._ano=int(input("enter AccountNo . of customer : ")) #_ano protected
        self.__cname=input("enter Customer Name : ") #__cname private
        self._balance=float(input("enter Balance : ")) # _balance : protected
    def display(self):
        print("Account No. :",self._ano)
        print("Customer Name : ",self.__cname)
        print("Balance : ",self._balance)

class Transaction(Customer):
        #Transaction derived class which inherits the features of base class
    def __init__(self): #constructor function
        super().__init__()#call constructor function of base class Customer 
        #super() inbuilt function
    def deposit(self):
        __a=int(input("enter Account No. to be deposit : ")) #__local private variable
        if(__a==self._ano):
            __amt=float(input("enter Deposit Amount : "))#__local private variable
            self._balance=self._balance+__amt
            print("Available Balance : ",self._balance)
            print("Amount deposit Successfully")
        else:
            print("Account No. Invalid : ")
    def withdrawl(self):
        __a=int(input("enter Account No. to be withdrawl : ")) #__local private variable
        if(__a==self._ano):
            __amt=float(input("enter Withdrawl Amount : "))  #local private variable
            if(__amt<self._balance):
                self._balance=self._balance-(__amt)
                print("Available Balance : ",self._balance)
                print("Amount Withdrawl Successfully")
                
            else:
                print("Insufficient balance ")
        else:
            print("Account No. Invalid : ")
    def check_balance(self):
        print("Balance : ",self._balance)
    def menu(self):
        print("1. Deposit \n 2. Withdrawl \n. 3. Chech Balance \n 4. Exit ")

#main program
        
tran=Transaction() #create object of Transaction derived class
tran.display()
#LOOP
while(True):
    tran.menu()
    ch=int(input("enter Your Choice : "))
    if(ch==1):
        tran.deposit()
    elif(ch==2):
        tran.withdrawl()
    elif(ch==3):
        tran.check_balance()
    else:
        break #ecit from loop

        
