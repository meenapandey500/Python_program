import calendar
y=int(input("Enter Year : "))
m=int(input("Enter Month : "))
cal=calendar.month(y,m) #month() inbuilt function of calendar module 
print(cal)
