from datetime import datetime
#import time
#t1=time.time()

t=datetime.now()  #to hold  current date and time
print("System time : ",t)
print("Only show Hours  from current date : ",t.hour)  #14 (by default set 24 hours)
# OR
print("Only show Hours  from current date : ",t.strftime("%H")) #14  (24 hours)
print("Only show Hours  from current date : ",t.strftime("%I%p")) #2  (IF 12 hours then use %I)  %p AM/PM
#minutes %M
print("Only show Minutes  from current date : ",t.strftime("%M"))
#seconds %S
print("Only show Seconds  from current date : ",t.strftime("%S"))

