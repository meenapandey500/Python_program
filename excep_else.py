# Program to depict else clause with try-except 

# Function which returns a/b 
def divide(a , b): 
	try: 
		c = ((a+b) / (a-b)) 
	except ZeroDivisionError: 
		print( "a/b result in 0")
	else: 
		print(c )

# Driver program to test above function 
divide(2.0, 3.0) 
divide(3.0, 3.0) 
