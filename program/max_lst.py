#WAP to store marks of 10 student of python subject and find the maximum marks and minimum marks from 10 students
python=[78,89,56,77,59,62,46,98,77,50]
max=0  #or max=python[0]
for x in python:
    print(x)
    if(max<x):   
        max=x

print("Maximum marks : ",max)

min=max #iniitialize  min=9999 or min=python[0]
for x in python:
    if(min>x) :   #98>78 true  min=x means min=78, 78>89 false  if(78>56) true min=x means min=56   56>46 means min=46
        min=x
print("Minimum marks : ",min)
