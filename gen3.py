'''for i in range(780000000000000000000):  #means start=0 bydefault  if no mension and stop=78-1  step=+1
    print(i)'''

def gen(n1):     #return /print( )/ yield
    for i in range(n1): #3
        yield i
        

#main program
g=gen(10)
print(g)
for i in g:
    print(i)
'''print(g.__next__()) 
print(g.__next__()) 
print(g.__next__())
print(g.__next__())'''
