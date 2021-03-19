#Write a program to find the simple interest and amount when given principal,rate and time
#Using function 1. passing arguments/parameters and return value
import lib
#main program
p=float(input("Enter Principal : "))
r=float(input("Enter Rate of Interest : "))
t=int(input("Enter Time : "))
#call function
si=lib.simple_interest(p,r,t)
a=lib.amount(p,si)
print("Simple Interest : ",si)
print("Amount : ",a)
