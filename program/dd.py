def accept_age(age):
    try:
       assert(age>=18),"age should not less than 18"
       print(age, "This is Valid Age : ")
    except AssertionError as er:
        print(er)
#main program
age=int(input("Enter Age "))
accept_age(age) #call function
