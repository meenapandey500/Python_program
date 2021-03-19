def simple_interest(p,r,t):
    return p*r*t/100

def amount(p,si):
    return p+si


def palindrom(n):
    r=0 #initial
    while(n>0):
      y=n%10
      r=r*10+y
      n=n//10
    return r

#create function to interchange the value of 2 variables
#using passing arguments/parameters but no return value
def swap(a,b):
    a,b=b,a  #without using temporary variable
    print("After Swapping a={} , b={}".format(a,b))
    
