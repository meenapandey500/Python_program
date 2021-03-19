#wap to find the square of first 10 natural no. and store in list .

#Without using List comprehension
answer=[ ]   #empty list declare
for  x in range(1,11):
        answer.append(x**2)
print("Square of list : ",answer)
   

#using list comprehension

answer=[x**2 for x in range(1,11)]
print("Square of list : ",answer)
