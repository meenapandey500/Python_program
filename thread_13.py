# using multithreading 
import time #time inbuilt library
import threading
def square(N): #passing arguments  but no return value
    print("\n Calculate Square of given numbers : ")
    for i in N: #N=[2,3,8,9]
        time.sleep(0.2) #0.2 second by default
        print("\n Square : ",i*i)

def cube(N): #passing arguments  but no return value
    print("Calculate cube of given numbers : ")
    for i in N:
        time.sleep(0.2) #0.2 second by default
        print("\n Cube : ",i*i*i)



#main program
#create the list object N
N=[2,3,8,9]
print(N)
t=time.time() # Create the object t of time()  : to retrieve current time of system
print("Time Before Process : ",t)

th1=threading.Thread(target=square,args=(N,))
th2=threading.Thread(target=cube,args=(N,))

th1.start()
#th1.join()
th2.start()
#th2.join()
t1=time.time()
print("Time After  Process : ",t1)
print("Done in : ",t1-t)  #time.time() : current time after process
print("Successfully done : ")



