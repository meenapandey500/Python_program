def gen(n) : #user defined function
    for i in range(n): #here start=0 stop=n-1 step=+1
        yield i   #yield create the genarator object in ram

#main program
#call function
g=gen(3)
print(g) #address of genearator g
'''print(g.__next__()) #0
print(g.__next__()) #1
print(g.__next__()) #2
print(g.__next__()) #3'''

#use Iterator
for x in g:
    print(x)

