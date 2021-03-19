class student:
    'this ts student class which hold all details of students and print it'
    def __init__(self): 
        print("Welcome student")
        self.rno=input("enter rollno")
        self.name=input("enter name ")
    def __del__(self): #destructor function : it is used to clear memory of object of class
        print("Memory clear")
#main program
print("documents of class : ",student.__doc__) #doc means document
print("variables in class : ",student.__dict__) #dict means dictionary
#create object of class
s=student()
del s  #call destructor function   : del object name
