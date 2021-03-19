#Example  Return a list containing every occurrence of  "come" . Then use findall( )
import re
#suppose assign string value in str variable
str="The rain in Spain"
print(str)
x=re.findall("come",str) #here x is a list object and hold ai if found in str variable
#syntax findall("pattern",string variablename)
print(x)
if(x):  #if found come in str variable means true
    print("Yes , there ia at least one match")
else:
    print("No match")
