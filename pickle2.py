#to store data from dictionary to file in binary format or use serialization
import pickle
t=open("student.txt","wb")
#create a dictionary
d={"Name":"Kamal","Age":23,"Gender":"Male","Marks":87}
pickle.dump(d,t) #dump(dicname,temp file)
t.close()

#To read data from file Deserialization 

t=open("student.txt","rb")
d=pickle.load(t) #load(temp file) and d is dict object , its hold data from file
print(d)
t.close()
