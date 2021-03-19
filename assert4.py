try:
    num=int(input('Enter a number: '))
    assert(num >=0), "Only positive numbers accepted."
    print(num)
except AssertionError as msg:
    print(msg)
