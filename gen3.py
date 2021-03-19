def gen(n) : #user defined function
    for i in range(n): 
        yield i   #yield create the genarator object in ram

#main program
#call function
g=gen(3)
print(g) #address of genearator g
for i in g:  #use iterator method
    print(i)


