from datetime import datetime
d="21 June, 2018"  #to store date of birth
print("DOB : ",d)    # 21-June,2018
print("Type of dob : ",type(d))
#To change string type data to date type  use inbuilt function strptime( )
d1=datetime.strptime(d , "%d  %B, %Y")
print("Date Of Birth : ",d1.year,"-",d1.month,"-",d1.day)
print("Type of DOB : ",type(d1))
