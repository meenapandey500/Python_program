a="1234567890"
my_iterator=iter(a)
print(my_iterator) #return object in hexa form this is memory location
#iteration return value 1 by 1
#iterator return the address of value not return value
'''print(next(my_iterator)) #next() retrieve the value which stored the address

print(next(my_iterator))'''

for i in iter(a):
    print(i)
