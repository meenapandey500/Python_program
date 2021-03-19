#use map( ) : inbuilt function of python ,it is used to send value from list variable to
#user defined function one by one according to index without using for loop
#syntax of map()
#map(userdefined functionname, list input variable)
def square(x): #square( ) user defined function
    return x**2

#create list 
N=[10,20,30,40,50] #here N is list object which is input  [ ]
s=list(map(square,N))  #call function
print(s)  #s=[100,400,900,1600,2500]
#s=[100]
#s=[100,400]
#s=[100,400,900]

#There are create list from 2 types :-
# 1. [ ]
# 2. list( )
