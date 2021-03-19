>>> import os
>>> os.getcwd()
'C:\\Users\\Rajesh\\AppData\\Local\\Programs\\Python\\Python38-32\\Bank-Management-System-Project-in-Python-master\\Bank-Management-System-Project-in-Python-master'
>>> os.mkdir("f://meena")
>>> os.chdir("f://meena")
>>> os.getcwd()
'f:\\meena'
>>> os.copy("f://msg.txt","f://meena")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    os.copy("f://msg.txt","f://meena")
AttributeError: module 'os' has no attribute 'copy'
>>> os.rename("f://msg.txt","f://meena//msg.txt")
>>> os.remove("f://meena//msg.txt")
>>> 
