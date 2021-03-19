#zip( ) : Atleast 2 list must be occurs 

str=['a' ,'b' ,'c' ,'d','e']
n=[1,2,3,4,5]

new_list=list(zip(str,n))
print(new_list)

res=list(zip(*new_list)) #* unzip
print(res)

