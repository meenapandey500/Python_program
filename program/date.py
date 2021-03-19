#WAP to display only system date  and also display current year only
from datetime import date

d=date.today( )  #to hold system date means current date
print("System date : ",d)
print("Only show year from current date : ",d.year)
#or format : strftime( )
print("Only show year from current date : ",d.strftime("%Y"))  #2020   str means string f means format time
#or
print("Only show year from current date : ",d.strftime("%y"))  #20
#month : for month or strftime(%m)
print("Only show month from current date : ",d.month)  #10 means october
print("Only show month from current date : ",d.strftime("%m")) #10 means october

print("Only show month from current date : ",d.strftime("%B")) #October : 10 
print("Only show month from current date : ",d.strftime("%b")) #oct

#For day
print("Only show date from current date : ",d.day)  #17
print("Only show date from current date : ",d.strftime("%d")) #17

#return weekday
print("Only show date from current date : ",d.strftime("%a")) #sat
print("Only show date from current date : ",d.strftime("%A"))#saturday

print("Only show date from current date : ",d.strftime("%w")) #monday=1 tues=2  sat=6
