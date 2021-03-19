#WAP TO PRINT THOSE NUMBERS FROM LIST WHOSE NOT DIVISIBLE BY 3 AND 7
A=[20,23,21,9,42,90,55] #list create
for x in A:
    if(x%3==0 and x%7==0):
        continue  #not print these no
    print(x)
        
