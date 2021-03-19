#create class Employee
class Employee :  #Employee user defined class name
    empid=101
    empname="renu gupta"
    mobile=9827373371
    salary=78000

#main program
print("Employee Id : {}\nEmployee Name : {}\nEmployees Mobile : {}\nEmployees Salary : {}".
     format(Employee.empid,Employee.empname,Employee.mobile,Employee.salary))
Employee.salary=90000
print("Employee salary : ",Employee.salary)

sales=Employee()  #create object of Employee class
print("Details Of Employee of sales : \n")
print("Employee Id : {}\nEmployee Name : {}\nEmployees Mobile : {}\nEmployees Salary : {}".
     format(sales.empid,sales.empname,sales.mobile,sales.salary))

service=Employee()
print("Details Of Employee of Service : \n")
print("Employee Id : {}\nEmployee Name : {}\nEmployees Mobile : {}\nEmployees Salary : {}".
     format(service.empid,service.empname,service.mobile,service.salary))
