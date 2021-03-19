#constructor overloading :
#constructor function :  __init__( ) : always defination for input ot for initialise the
#value of variable , it is automatIC CALL when create a object of class

class School: #School class user defined
    def __init__(self,id=None,name=None,course=None,mobile=None,desig=None,salary=None):
        #parameter constructor
        if(id!=None and name!=None and course!=None and mobile!=None and
            desig==None and salary==None):
            self.id=id
            self.name=name
            self.course=course
            self.mobile=mobile
        elif(id!=None and name!=None and course!=None and mobile!=None and
            desig!=None and salary!=None):
            self.id=id
            self.name=name
            self.course=course
            self.mobile=mobile
            self.desig=desig
            self.salary=salary
        else:
            print("invalid")
            
    def show_student(self):
        print("Details of student : ")
        print("Enrollment No. : ",self.id)
        print("Student Name : ",self.name)
        print("Course Name : ",self.course)
        print("Mobile No. : ",self.mobile)
        
    def show_teacher(self):
        print("Details of Employees : ")
        print("Employee No. : ",self.id)
        print("Employee Name : ",self.name)
        print("Teach Course Name : ",self.course)
        print("Employees Mobile No. : ",self.mobile)
        print("Designation : ",self.desig)
        print("Employee Salary : ",self.salary)


#main program
print("Enter the details of student : ")
enroll=int(input("Enter enrollment no. : "))
sname=input("Enter Student Name : ")
c=input("Enter course name : ")
m=int(input("Enter mobile no. "))
student=School(enroll,sname,c,m)

student.show_student() #call method

print("Enter the details of Teacher : ")
tid=int(input("Enter Teacher Id. : "))
tname=input("Enter Teacher Name : ")
c=input("Enter course name to teach: ")
m=int(input("Enter mobile no. of teacher  "))
d=input("Enter Desigmation of teacher : ")
s=float(input("Enter Salary : "))
#create object of school
teacher=School(tid,tname,c,m,d,s)
teacher.show_teacher() #call


        
        
