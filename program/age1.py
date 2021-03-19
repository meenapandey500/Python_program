def accept_age(age):
    try:
        if(age<18):
            raise ValueError("age should not less than 18")
    except ValueError as v:
        print(v)
    else:
        print(age)
