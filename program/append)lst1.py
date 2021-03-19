#WAP to add element in add on runtime 
python=[] #declare empty list
while(True):
    marks=int(input("Enter Marks of python of student "))
    python.append(marks)
   
    ans=input("Add another marks of student if press n for No: ")
    if(ans=="n"):
        break #exit from loop

print(python)

