from employees import Employee
#here employees.py file  and Employee class
#create object of class Employee
sales=Employee()
trainer=Employee()
peon=Employee()
account=Employee()
admin=Employee()

print("Enter details of sale's person")
sales.getdata()
print("Details of sales person")
sales.display()
print("Enter details of Trainer ")
trainer.getdata()
print(" details of Trainer ")
trainer.display()

peon.getdata()
peon.display()

account.getdata()
account.display()

admin.getdata()
admin.display()
