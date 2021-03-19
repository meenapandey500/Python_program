with open("employee.csv","a") as t: #t temporary file
    eno=int(input("Enter Employee No. :"))
    name=input("Enter Employee name : ")
    data=str(eno)+','+name+'\n'  #file store data in string format
    t.write(data)

print("File create successfully")


