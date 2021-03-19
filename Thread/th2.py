import time #time inbuilt package
import threading #inbuilt package
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
# using Thread

#create object of time
t1=time.time() #current time before call
print("\n current time before call : ", t1)
#create object of Thread class th1
th1=threading.Thread(target=square,args=(num,))
#create object of Thread class th2
th2=threading.Thread(target=cube,args=(num,))

#start thread
th1.start()  #start() inbuilt function of Thread class
th1.join() #join() inbuilt function of Thread class
th2.start()
th2.join()
t2=time.time()-t1 #current time After call
print("\n Done in  : ", t2)
print("\n Complete ")
