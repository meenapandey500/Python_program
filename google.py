'''Write a Python program to count the number of characters (character frequency) in a string

Sample String : 'google.com'
output :
{'g' : 2 ,'0':2 ,l:1  e: 1  c: 1 m :1}
'''
def character_frequency(str):  #str=google.com
    #create empty dictionary
    dict={ }
    for i in str:   #i=g  next i=o next i=o
        k=dict.keys()  #K='g' ,'o' 
        if i in k : 
            dict[i]+=1  
        else:
            dict[i]=1
    return dict

#main program
str="google.com"
#call function
d=character_frequency(str)
print(d)
print(d.keys()) #keys() inbuilt function of dictionary
print(d.values()) #values() inbuilt function of dictionary
