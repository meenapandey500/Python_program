import time #time inbuilt class
def square(num): #passing arguments  num=[1,2,3,4]
    print("Calculate Square of Given Numbers num")
    for i in num:
        print("Square : ",i*i)

def cube(num):#passing arguments  num=[1,2,3,4]
    print("Calculate Cube of Given Numbers num")
    for i in num:
        print("Cube : ",i*i*i)



#main program
num=[1,2,3,4] #num is a list object
#Without using Thread
#create object of time
t1=time.time() #current time before call
print("\n current time before call : ", t1)
square(num) #call function
print("\n current time after complete square : ", time.time())
cube(num)#call function
print("\n current time after complete cube: ", time.time())
t2=time.time()-t1 #current time After call
print("\n Done in  : ", t2)
print("\n Complete ")
