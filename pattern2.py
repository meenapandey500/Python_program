#pattern matching
x=1 #line initialize
while(x<=5):  #outer loop
    y=1 #column initialize
    while(y<=5-x):    #inner loop  this loop  use left the space
        print(" ",end="")
        y=y+1
    k=x
    while(k>=1): #inner loop  
        print(k,end="")  
        k=k-1
    x=x+1 #line increment by 1
    print() #goto cursor on new line
