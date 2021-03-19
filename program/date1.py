import datetime
d=datetime.date(2008,5,24)  #format yyyy-mm-dd)
print(d)
print("Datatype of d : ",type(d))
print(d.day,"/",d.month,"/",d.year)
#or
print(d.day,"-",d.strftime("%B"),"-",d.year)
# OR
print(d.strftime("%A"),",",d.day,"-",d.strftime("%B"),"-",d.year)
