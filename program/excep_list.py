#Example of Exception Handling
#suppose create a list
X=[10,20,30]
try:
    print("Value at first location : ",X[0])
    print("Value at second location : ",X[1])
    print("Value at Third location : ",X[2])
    print("Value at Fourth location : ",X[3])
except IndexError:
    print("Out of index")
